__all__ = [
    'BasePoolMetric',
    'AssignmentEventsInPool',
    'AssignmentsInPool',
    'BansInPool',
    'PoolCompletedPercentage',
    'SpentBudgetOnPool',
    'TasksInPool',
    'WorkersByFilterOnPool',
]

from collections import defaultdict
import datetime
from functools import lru_cache
from itertools import groupby
from operator import attrgetter
import sys

if sys.version_info[:2] >= (3, 8):
    from functools import cached_property
else:
    from cached_property import cached_property

import attr
from typing import Any, Optional, Dict, List, Tuple
from ..client import (
    TolokaClient,
    Pool,
)
from ..client import analytics_request
from ..client.operations import Operation
from ..client._converter import structure
from ..streaming import cursor
from .metrics import BaseMetric


@lru_cache(maxsize=128)
def get_pool(pool_id: str, toloka_client: TolokaClient) -> Pool:
    return toloka_client.get_pool(pool_id)


@attr.s(auto_attribs=True)
class BasePoolMetric(BaseMetric):
    """Base class for all pool metrics"""
    pool_id : str = attr.ib(kw_only=False)

    @cached_property
    def beautiful_name(self) -> str:
        name = super(BasePoolMetric, self).beautiful_name
        pool = get_pool(self.pool_id, self.toloka_client)
        return f'{name} \'{pool.private_name}\' ({pool.id})'


@attr.s(auto_attribs=True)
class AssignmentEventsInPool(BasePoolMetric):
    """Tracking the change of response statuses in the pool.
    The metric is convenient for tracking that the pool is generally "alive" and working.
    If you want to track assignments counts, it's better to use AssignmentsInPool.

    Metrics starts gathering if they name are set. If the metric name is set to None, they don't gathering.

    Args:
        pool_id: From which pool track metrics.
        created_name: Metric name for a count of created events. Default None.
        submitted_name: Metric name for a count of submitted events. Default 'submitted_events_in_pool'.
        accepted_name : Metric name for a count of accepted events. Default 'accepted_events_in_pool'.
        rejected_name : Metric name for a count of rejected events. Default 'rejected_events_in_pool'.
        skipped_name: Metric name for a count of skipped events. Default None.
        expired_name: Metric name for a count of expired events. Default None.
        join_events: Count all events in one point.  Default False.

    Raises:
        ValueError: If all metric names are set to None or if there are duplicate metric names.

    Example:
        How to collect this metrics:
        >>> def print_metric(metric_dict):
        >>>     print(metric_dict)
        >>>
        >>> collector = MetricCollector([AssignmentEventsInPool(pool_id, toloka_client=toloka_client)], print_metric)
        >>> asyncio.run(collector.run())
        {
            'submitted_events_in_pool': [(datetime.datetime(2021, 8, 11, 15, 13, 4, 31000), 5)],
            'accepted_events_in_pool': [(datetime.datetime(2021, 8, 11, 15, 13, 3, 65000), 1)],
            'rejected_events_in_pool': [],
        }
    """
    _created_name : Optional[str] = None
    _submitted_name : Optional[str] = None
    _accepted_name : Optional[str] = None
    _rejected_name : Optional[str] = None
    _skipped_name : Optional[str] = None
    _expired_name : Optional[str] = None

    _join_events : bool = False

    _status_dict = {
        '_created_name': 'CREATED',
        '_submitted_name': 'SUBMITTED',
        '_accepted_name': 'ACCEPTED',
        '_rejected_name': 'REJECTED',
        '_skipped_name': 'SKIPPED',
        '_expired_name': 'EXPIRED',
    }

    def __attrs_post_init__(self):
        metric_names = self.get_line_names()
        if not metric_names:
            self._submitted_name = 'submitted_events_in_pool'
            self._accepted_name = 'accepted_events_in_pool'
            self._rejected_name = 'rejected_events_in_pool'
        elif len(metric_names) != len(set(metric_names)):
            raise ValueError('Duplicate metric names.')

    def get_line_names(self) -> List[str]:
        """Returns a list of metric names that can be generated by this class instance.
        """
        return [getattr(self, attr_name) for attr_name in self._status_dict if getattr(self, attr_name) is not None]

    @cached_property
    def _cursors(self) -> Dict[str, cursor.AssignmentCursor]:
        # key - metric name. One of the value of paramets: created_name, submitted_name, etc.
        # val - cursor configured for gathering this metric
        cursors = {}
        start_time = datetime.datetime.utcnow()
        for attr_name, status_value in self._status_dict.items():
            metric_name = getattr(self, attr_name)
            if metric_name:
                cursors[metric_name] = cursor.AssignmentCursor(
                    pool_id=self.pool_id,
                    event_type=status_value,
                    toloka_client=self.atoloka_client,
                    **{f'{status_value.lower()}_gte': start_time},
                )
        return cursors

    async def _get_lines_impl(self) -> Dict[str, List[Tuple[Any, Any]]]:
        result = {}
        for metric_name, it in self._cursors.items():
            event_list = [event async for event in it]
            if self._join_events:
                count = len(event_list)
                result[metric_name] = [(event_list[-1].event_time, count)] if count else [(datetime.datetime.utcnow(), 0)]
            else:
                result[metric_name] = [
                    (event_time, len(events))
                    for event_time, events in groupby(event_list, attrgetter('event_time'))
                ]
        return result


@attr.s(auto_attribs=True)
class PoolCompletedPercentage(BasePoolMetric):
    """Track pool completion in percentage

    Args:
        pool_id: From which pool track metrics.
        percents_name: Metric name for pool completion percentage. Default 'completion_percentage'.
        toloka_client: Client for connection to Toloka. You can set toloka_client for several metrics via "bind_client" function.

    Example:
        How to collect this metric:
        >>> def print_metric(metric_dict):
        >>>     print(metric_dict)
        >>>
        >>> collector = MetricCollector([PoolCompletedPercentage(pool_id, toloka_client=toloka_client)], print_metric)
        >>> asyncio.run(collector.run())
        {
            'completion_percentage': [(datetime.datetime(2021, 8, 11, 15, 13, 4, 31000), 55)],
        }
    """
    _percents_name : Optional[str] = None

    def __attrs_post_init__(self):
        if self._percents_name is None:
            self._percents_name = 'completion_percentage'

    def get_line_names(self) -> List[str]:
        """Returns a list of metric names that can be generated by this class instance.
        """
        return [self._percents_name]

    async def _get_lines_impl(self) -> Dict[str, List[Tuple[Any, Any]]]:
        result = {}
        operation = await self.atoloka_client.get_analytics([analytics_request.CompletionPercentagePoolAnalytics(subject_id=self.pool_id)])
        operation = await self.atoloka_client.wait_operation(operation)

        if operation.status == Operation.Status.SUCCESS:
            for response in operation.details['value']:
                result[self._percents_name] = [(structure(response['finished'], datetime.datetime), response['result']['value'])]

        return result


@attr.s(auto_attribs=True)
class AssignmentsInPool(BasePoolMetric):
    """Tracking the count of assignments in different states in the pool.

    Metrics starts gathering if they name are set. If the metric name is set to None, they don't gathering.

    Args:
        pool_id: From which pool track metrics.
        submitted_name: Metric name for a count of submitted assignments. Default 'submitted_assignments_in_pool'.
        accepted_name : Metric name for a count of accepted assignments. Default 'accepted_assignments_in_pool'.
        rejected_name : Metric name for a count of rejected assignments. Default 'rejected_assignments_in_pool'.
        skipped_name: Metric name for a count of skipped assignments. Default None.

    Raises:
        ValueError: If some metric has same names.

    Example:
        How to collect this metrics:
        >>> def print_metric(metric_dict):
        >>>     print(metric_dict)
        >>>
        >>> collector = MetricCollector([AssignmentsInPool(pool_id, toloka_client=toloka_client)], print_metric)
        >>> asyncio.run(collector.run())
        {
            'rejected_assignments_in_pool': [(datetime.datetime(2021, 8, 12, 10, 4, 44, 895232), 0)],
            'submitted_assignments_in_pool': [(datetime.datetime(2021, 8, 12, 10, 4, 45, 321904), 75)],
            'accepted_assignments_in_pool': [(datetime.datetime(2021, 8, 12, 10, 4, 45, 951156), 75)],
        }
    """
    _submitted_name : Optional[str] = None
    _accepted_name : Optional[str] = None
    _rejected_name : Optional[str] = None
    _skipped_name : Optional[str] = None

    _analytics_dict = {
        '_submitted_name': analytics_request.SubmitedAssignmentsCountPoolAnalytics,
        '_accepted_name': analytics_request.ApprovedAssignmentsCountPoolAnalytics,
        '_rejected_name': analytics_request.RejectedAssignmentsCountPoolAnalytics,
        '_skipped_name': analytics_request.SkippedAssignmentsCountPoolAnalytics,
    }

    def __attrs_post_init__(self):
        metric_names = self.get_line_names()
        if not metric_names:
            self._submitted_name = 'submitted_assignments_in_pool'
            self._accepted_name = 'accepted_assignments_in_pool'
            self._rejected_name = 'rejected_assignments_in_pool'
        elif len(metric_names) != len(set(metric_names)):
            raise ValueError('Duplicate metric names.')

    def get_line_names(self) -> List[str]:
        """Returns a list of metric names that can be generated by this class instance.
        """
        return [getattr(self, attr_name) for attr_name in self._analytics_dict if getattr(self, attr_name) is not None]

    @cached_property
    def _analytics_request(self) -> List[analytics_request.PoolAnalyticsRequest]:
        analytics_for_request = []
        for attr_name, analytic in self._analytics_dict.items():
            attr_val = getattr(self, attr_name)
            if attr_val:
                analytics_for_request.append(analytic(subject_id=self.pool_id))

        return analytics_for_request

    @cached_property
    def _analytic_classes_to_metric_names(self) -> Dict[str, str]:
        return {str(analytic_class.name.value): field_name for field_name, analytic_class in self._analytics_dict.items()}

    async def _get_lines_impl(self) -> Dict[str, List[Tuple[Any, Any]]]:
        result = {}
        operation = await self.atoloka_client.get_analytics(self._analytics_request)
        operation = await self.atoloka_client.wait_operation(operation)

        if operation.status == Operation.Status.SUCCESS:
            for response in operation.details['value']:
                metric_name = response['request']['name']
                metric_name = self._analytic_classes_to_metric_names[metric_name]
                metric_name = getattr(self, metric_name)
                result[metric_name] = [(structure(response['finished'], datetime.datetime), response['result'])]

        return result


@attr.s(auto_attribs=True)
class TasksInPool(BasePoolMetric):
    """The number of tasks in the pool. Not new tasks. All tasks on each step.

    Args:
        pool_id: From which pool track metrics.
        tasks_name: Metric name for a count of tasks.

    Example:
        How to collect this metrics:
        >>> def print_metric(metric_dict):
        >>>     print(metric_dict)
        >>>
        >>> collector = MetricCollector([TasksInPool(pool_id, toloka_client=toloka_client)], print_metric)
        >>> asyncio.run(collector.run())
        {
            'tasks_count': [(datetime.datetime(2021, 11, 18, 9, 36, 34, 163000), 40)],
        }
    """
    _tasks_name : Optional[str] = None

    def __attrs_post_init__(self):
        if self._tasks_name is None:
            self._tasks_name = 'tasks_count'

    def get_line_names(self) -> List[str]:
        """Returns a list of metric names that can be generated by this class instance.
        """
        return [self._tasks_name]

    async def _get_lines_impl(self) -> Dict[str, List[Tuple[Any, Any]]]:
        result = {}
        operation = await self.atoloka_client.get_analytics([analytics_request.RealTasksCountPoolAnalytics(subject_id=self.pool_id)])
        operation = await self.atoloka_client.wait_operation(operation)

        if operation.status == Operation.Status.SUCCESS:
            for response in operation.details['value']:
                # response = {'result': 40, 'request': {'name': 'real_tasks_count', 'subject': 'POOL', 'subject_id': '29158096'}, 'finished': '2021-11-18T09:33:54.388'}
                result[self._tasks_name] = [(structure(response['finished'], datetime.datetime), response['result'])]

        return result


@attr.s(auto_attribs=True)
class SpentBudgetOnPool(BasePoolMetric):
    """How much money has already been spent on this pool, excluding fee.

    Args:
        pool_id: From which pool track metrics.
        tasks_name: Metric name for a count of tasks.

    Example:
        How to collect this metrics:
        >>> def print_metric(metric_dict):
        >>>     print(metric_dict)
        >>>
        >>> collector = MetricCollector([SpentBudgetOnPool(pool_id, toloka_client=toloka_client)], print_metric)
        >>> asyncio.run(collector.run())
        {
            'spent_money': [(datetime.datetime(2021, 11, 18, 9, 36, 34, 163000), Decimal('0.3'))],
        }
    """
    _money_name : Optional[str] = None

    def __attrs_post_init__(self):
        if self._money_name is None:
            self._money_name = 'spent_money'

    def get_line_names(self) -> List[str]:
        """Returns a list of metric names that can be generated by this class instance.
        """
        return [self._money_name]

    async def _get_lines_impl(self) -> Dict[str, List[Tuple[Any, Any]]]:
        result = {}
        operation = await self.atoloka_client.get_analytics([analytics_request.SpentBudgetPoolAnalytics(subject_id=self.pool_id)])
        operation = await self.atoloka_client.wait_operation(operation)

        if operation.status == Operation.Status.SUCCESS:
            for response in operation.details['value']:
                # response = {'result': Decimal('0.3'), 'request': {'name': 'spent_budget', 'subject': 'POOL', 'subject_id': '29158096'}, 'finished': '2021-11-18T09:38:30.401'}
                result[self._money_name] = [(structure(response['finished'], datetime.datetime), response['result'])]

        return result


@attr.s(auto_attribs=True)
class WorkersByFilterOnPool(BasePoolMetric):
    """The number of active performers matching the pool filters for the last hours (default 1 hour)

    Args:
        pool_id: From which pool track metrics.
        workers_name: Metric name for a count of workers.
        interval_hours: Counts unical workers on this hours interval. Default 1.

    Example:
        How to collect this metrics:
        >>> def print_metric(metric_dict):
        >>>     print(metric_dict)
        >>>
        >>> collector = MetricCollector([WorkersByFilterOnPool(pool_id, toloka_client=toloka_client)], print_metric)
        >>> asyncio.run(collector.run())
        {
            'workers_count': [(datetime.datetime(2021, 11, 18, 9, 36, 34, 163000), 2697)],
        }
    """
    _workers_name : Optional[str] = None
    _interval_hours: int = attr.ib(default=1)

    def __attrs_post_init__(self):
        if self._workers_name is None:
            self._workers_name = 'workers_count'

    def get_line_names(self) -> List[str]:
        """Returns a list of metric names that can be generated by this class instance.
        """
        return [self._workers_name]

    async def _get_lines_impl(self) -> Dict[str, List[Tuple[Any, Any]]]:
        result = {}
        operation = await self.atoloka_client.get_analytics(
            [analytics_request.ActiveWorkersByFilterCountPoolAnalytics(subject_id=self.pool_id, interval_hours=self._interval_hours)]
        )
        operation = await self.atoloka_client.wait_operation(operation)

        if operation.status == Operation.Status.SUCCESS:
            for response in operation.details['value']:
                # response = {
                #   'result': 0,
                #   'request': {'name': 'active_workers_by_filter_count', 'subject': 'POOL', 'subject_id': '29158096', 'interval_hours': 1},
                #   'finished': '2021-11-18T09:41:01.777'
                # }
                result[self._workers_name] = [(structure(response['finished'], datetime.datetime), response['result'])]

        return result


@attr.s(auto_attribs=True)
class BansInPool(BasePoolMetric):
    """Tracking the new user restrictions in pool

    Be careful: if you set in quality controls to ban performers 'on project', bans 'on pool' will never happen.

    Args:
        pool_id: From which pool track metrics.
        count_name: Metric name for a count of bans.
        filter_by_comment: Allow to split user restriction into several lines based on comment.
            Dictionary where, key - comment string, and value - name for line in which will be aggregated bans with this comments.
        join_events: Count all events in one point.  Default False.

    Example:
        How to collect this metrics:
        >>> def print_metric(metric_dict):
        >>>     print(metric_dict)
        >>>
        >>> collector = MetricCollector([BansInPool(pool_id, toloka_client=toloka_client)], print_metric)
        >>> asyncio.run(collector.run())
        {
            'bans_count': [(datetime.datetime(2021, 11, 18, 13, 30, 11, 522000), 1)],
        }

        How to split bans onto several metrics.
        >>> collector = MetricCollector(
        >>>     [
        >>>         BansInPool(
        >>>             pool_id,
        >>>             toloka_client=toloka_client,
        >>>             filter_by_comment={'fast answers': 'fast', 'bad quality on honeypots': 'honeypots'}
        >>>         ),
        >>>     ],
        >>>     print_metric
        >>> )
        >>> asyncio.run(collector.run())
        {
            'honeypots': [(datetime.datetime(2021, 11, 18, 13, 32, 52, 475000), 1)],
            'fast': [(datetime.datetime(2021, 11, 18, 13, 32, 50, 453000), 1)],
        }
    """
    _count_name : Optional[str] = None
    _filter_by_comment : Optional[Dict[str, str]] = None  # {'comment': 'line_name'}

    _join_events : bool = False

    def __attrs_post_init__(self):
        metric_names = self.get_line_names()
        if not metric_names:
            self._count_name = 'bans_count'
        if not self._filter_by_comment:
            self._filter_by_comment = None

    def get_line_names(self) -> List[str]:
        """Returns a list of metric names that can be generated by this class instance.
        """
        line_names = self._filter_by_comment.values() if self._filter_by_comment is not None else []
        if self._count_name is not None:
            line_names.append(self._count_name)
        return line_names

    @cached_property
    def _cursor(self) -> cursor.UserRestrictionCursor:
        return cursor.UserRestrictionCursor(
            toloka_client=self.atoloka_client,
            created_gte=datetime.datetime.utcnow(),
            pool_id=self.pool_id
        )

    async def _get_lines_impl(self) -> Dict[str, List[Tuple[Any, Any]]]:
        result = defaultdict(list)

        it = self._cursor
        event_list = [event async for event in it]
        if self._join_events:
            if self._count_name is not None:
                result[self._count_name] = [(event_list[-1].event_time, len(event_list))] if event_list else [(datetime.datetime.utcnow(), 0)]
            if self._filter_by_comment is not None:
                comments_count = defaultdict(int)
                for event in event_list:
                    comments_count[event.user_restriction.private_comment] += 1
                for comment, line_name in self._filter_by_comment.items():
                    result[line_name] = [(datetime.datetime.utcnow(), comments_count[comment] if comment in comments_count else 0)]
        else:
            if self._count_name is not None:
                result[self._count_name] = [
                    (event_time, len(events))
                    for event_time, events in groupby(event_list, attrgetter('event_time'))
                ]
            if self._filter_by_comment is not None:
                for comment, events in groupby(event_list, attrgetter('user_restriction.private_comment')):
                    if comment in self._filter_by_comment:
                        result[self._filter_by_comment[comment]].extend(
                            [
                                (event_time, len(sub_events))
                                for event_time, sub_events in groupby(events, attrgetter('event_time'))
                            ]
                        )

        return result
