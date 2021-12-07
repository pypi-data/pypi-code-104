# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from bosdyn.api.spot import choreography_sequence_pb2 as bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2


class ChoreographyServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListAllMoves = channel.unary_unary(
        '/bosdyn.api.spot.ChoreographyService/ListAllMoves',
        request_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.ListAllMovesRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.ListAllMovesResponse.FromString,
        )
    self.UploadChoreography = channel.unary_unary(
        '/bosdyn.api.spot.ChoreographyService/UploadChoreography',
        request_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.UploadChoreographyRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.UploadChoreographyResponse.FromString,
        )
    self.UploadAnimatedMove = channel.unary_unary(
        '/bosdyn.api.spot.ChoreographyService/UploadAnimatedMove',
        request_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.UploadAnimatedMoveRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.UploadAnimatedMoveResponse.FromString,
        )
    self.ExecuteChoreography = channel.unary_unary(
        '/bosdyn.api.spot.ChoreographyService/ExecuteChoreography',
        request_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.ExecuteChoreographyRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.ExecuteChoreographyResponse.FromString,
        )
    self.StartRecordingState = channel.unary_unary(
        '/bosdyn.api.spot.ChoreographyService/StartRecordingState',
        request_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.StartRecordingStateRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.StartRecordingStateResponse.FromString,
        )
    self.StopRecordingState = channel.unary_unary(
        '/bosdyn.api.spot.ChoreographyService/StopRecordingState',
        request_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.StopRecordingStateRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.StopRecordingStateResponse.FromString,
        )
    self.DownloadRobotStateLog = channel.unary_stream(
        '/bosdyn.api.spot.ChoreographyService/DownloadRobotStateLog',
        request_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.DownloadRobotStateLogRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.DownloadRobotStateLogResponse.FromString,
        )


class ChoreographyServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListAllMoves(self, request, context):
    """List the available dance moves and their parameter information.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadChoreography(self, request, context):
    """Upload a dance to the robot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UploadAnimatedMove(self, request, context):
    """Upload an animation to the robot.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteChoreography(self, request, context):
    """Execute the uploaded dance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartRecordingState(self, request, context):
    """Manually start (or continue) recording the robot state.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopRecordingState(self, request, context):
    """Manually stop recording the robot state.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadRobotStateLog(self, request, context):
    """Download log of the latest recorded robot state information.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChoreographyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListAllMoves': grpc.unary_unary_rpc_method_handler(
          servicer.ListAllMoves,
          request_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.ListAllMovesRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.ListAllMovesResponse.SerializeToString,
      ),
      'UploadChoreography': grpc.unary_unary_rpc_method_handler(
          servicer.UploadChoreography,
          request_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.UploadChoreographyRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.UploadChoreographyResponse.SerializeToString,
      ),
      'UploadAnimatedMove': grpc.unary_unary_rpc_method_handler(
          servicer.UploadAnimatedMove,
          request_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.UploadAnimatedMoveRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.UploadAnimatedMoveResponse.SerializeToString,
      ),
      'ExecuteChoreography': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteChoreography,
          request_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.ExecuteChoreographyRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.ExecuteChoreographyResponse.SerializeToString,
      ),
      'StartRecordingState': grpc.unary_unary_rpc_method_handler(
          servicer.StartRecordingState,
          request_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.StartRecordingStateRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.StartRecordingStateResponse.SerializeToString,
      ),
      'StopRecordingState': grpc.unary_unary_rpc_method_handler(
          servicer.StopRecordingState,
          request_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.StopRecordingStateRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.StopRecordingStateResponse.SerializeToString,
      ),
      'DownloadRobotStateLog': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadRobotStateLog,
          request_deserializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.DownloadRobotStateLogRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_spot_dot_choreography__sequence__pb2.DownloadRobotStateLogResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bosdyn.api.spot.ChoreographyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
