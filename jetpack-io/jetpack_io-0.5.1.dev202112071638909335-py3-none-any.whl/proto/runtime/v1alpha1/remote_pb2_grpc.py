# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from jetpack.proto.runtime.v1alpha1 import remote_pb2 as jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2


class RemoteExecutorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateTask = channel.unary_unary(
                '/remote.RemoteExecutor/CreateTask',
                request_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.CreateTaskRequest.SerializeToString,
                response_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.CreateTaskResponse.FromString,
                )
        self.PostResult = channel.unary_unary(
                '/remote.RemoteExecutor/PostResult',
                request_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.PostResultRequest.SerializeToString,
                response_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.PostResultResponse.FromString,
                )
        self.WaitForResult = channel.unary_unary(
                '/remote.RemoteExecutor/WaitForResult',
                request_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.WaitForResultRequest.SerializeToString,
                response_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.WaitForResultResponse.FromString,
                )
        self.SetCronJobs = channel.unary_unary(
                '/remote.RemoteExecutor/SetCronJobs',
                request_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.SetCronJobsRequest.SerializeToString,
                response_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.SetCronJobsResponse.FromString,
                )
        self.RemoteCall = channel.unary_unary(
                '/remote.RemoteExecutor/RemoteCall',
                request_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.RemoteCallRequest.SerializeToString,
                response_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.RemoteCallResponse.FromString,
                )


class RemoteExecutorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PostResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitForResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCronJobs(self, request, context):
        """Sets the cron jobs associated to an app. If the list of cron jobs is
        empty, removes all the cron jobs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoteCall(self, request, context):
        """Golang prototype
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteExecutorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTask,
                    request_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.CreateTaskRequest.FromString,
                    response_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.CreateTaskResponse.SerializeToString,
            ),
            'PostResult': grpc.unary_unary_rpc_method_handler(
                    servicer.PostResult,
                    request_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.PostResultRequest.FromString,
                    response_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.PostResultResponse.SerializeToString,
            ),
            'WaitForResult': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitForResult,
                    request_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.WaitForResultRequest.FromString,
                    response_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.WaitForResultResponse.SerializeToString,
            ),
            'SetCronJobs': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCronJobs,
                    request_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.SetCronJobsRequest.FromString,
                    response_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.SetCronJobsResponse.SerializeToString,
            ),
            'RemoteCall': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoteCall,
                    request_deserializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.RemoteCallRequest.FromString,
                    response_serializer=jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.RemoteCallResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'remote.RemoteExecutor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoteExecutor(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.RemoteExecutor/CreateTask',
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.CreateTaskRequest.SerializeToString,
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.CreateTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PostResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.RemoteExecutor/PostResult',
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.PostResultRequest.SerializeToString,
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.PostResultResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitForResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.RemoteExecutor/WaitForResult',
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.WaitForResultRequest.SerializeToString,
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.WaitForResultResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCronJobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.RemoteExecutor/SetCronJobs',
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.SetCronJobsRequest.SerializeToString,
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.SetCronJobsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoteCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/remote.RemoteExecutor/RemoteCall',
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.RemoteCallRequest.SerializeToString,
            jetpack_dot_proto_dot_runtime_dot_v1alpha1_dot_remote__pb2.RemoteCallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
