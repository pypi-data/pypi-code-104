import time
import asyncio

from asyncio import Future, Queue, wait_for, Task
from functools import partial
from typing import AsyncIterator, Awaitable, Dict, Tuple

from ..model import MLModel
from ..types import (
    InferenceRequest,
    InferenceResponse,
)
from ..utils import generate_uuid

from .requests import BatchedRequests


class AdaptiveBatcher:
    def __init__(self, model: MLModel):
        self._model = model

        self._max_batch_size = model.settings.max_batch_size
        self._max_batch_time = model.settings.max_batch_time

        # Save predict function before it gets decorated
        self._predict_fn = model.predict
        self._requests: Queue[Tuple[str, InferenceRequest]] = Queue(
            maxsize=self._max_batch_size
        )
        self._async_responses: Dict[str, Future[InferenceResponse]] = {}
        self._batching_task = None

    async def predict(self, req: InferenceRequest) -> InferenceResponse:
        internal_id, _ = await self._queue_request(req)
        self._start_batcher_if_needed()
        return await self._wait_response(internal_id)

    async def _queue_request(
        self,
        req: InferenceRequest,
    ) -> Tuple[str, Awaitable[InferenceResponse]]:
        internal_id = generate_uuid()
        await self._requests.put((internal_id, req))

        loop = asyncio.get_running_loop()
        async_response = loop.create_future()
        self._async_responses[internal_id] = async_response

        return internal_id, async_response

    async def _wait_response(self, internal_id: str) -> InferenceResponse:
        async_response = self._async_responses[internal_id]

        try:
            response = await async_response
            return response
        finally:
            del self._async_responses[internal_id]

    def _start_batcher_if_needed(self):
        if self._batching_task is not None:
            if not self._batching_task.done():
                # If task hasn't finished yet, let it keep running
                return

        self._batching_task = asyncio.create_task(self._batcher())
        self._batching_task.add_done_callback(self._batching_task_callback)

    def _batching_task_callback(self, batching_task: Task):
        err = batching_task.exception()
        if err:
            # Clear queue
            self._clear_queue(err)

    def _clear_queue(self, err: BaseException):
        # Cancel all pending async responses
        for async_response in self._async_responses.values():
            async_response.set_exception(err)

        # Empty queue
        for _ in range(self._requests.qsize()):
            self._requests.get_nowait()

    async def _batcher(self):
        async for batched in self._batch_requests():
            # We run prediction as a Task to ensure it gets scheduled
            # immediately.
            # That way, we can process multiple batches concurrently.
            predict_task = asyncio.create_task(self._predict_fn(batched.merged_request))
            predict_task.add_done_callback(partial(self._predict_callback, batched))

    def _predict_callback(self, batched: BatchedRequests, predict_task: Task):
        try:
            batched_response = predict_task.result()
            responses = batched.split_response(batched_response)
            for internal_id, response in responses.items():
                self._async_responses[internal_id].set_result(response)
        except Exception as err:
            for internal_id in batched.inference_requests.keys():
                self._async_responses[internal_id].set_exception(err)

    async def _batch_requests(self) -> AsyncIterator[BatchedRequests]:
        while not self._requests.empty():
            to_batch: Dict[str, InferenceRequest] = {}
            start = time.time()
            timeout = self._max_batch_time

            try:
                while len(to_batch) < self._max_batch_size:
                    read_op = self._requests.get()
                    internal_id, inference_request = await wait_for(
                        read_op, timeout=timeout
                    )
                    to_batch[internal_id] = inference_request

                    # Update remaining timeout
                    current = time.time()
                    timeout = timeout - (current - start)
            except asyncio.TimeoutError:
                # NOTE: Hit timeout, continue
                pass

            yield BatchedRequests(to_batch)
