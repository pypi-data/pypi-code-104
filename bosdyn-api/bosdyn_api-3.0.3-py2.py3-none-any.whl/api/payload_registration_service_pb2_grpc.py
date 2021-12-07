# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from bosdyn.api import payload_registration_pb2 as bosdyn_dot_api_dot_payload__registration__pb2


class PayloadRegistrationServiceStub(object):
  """This service provides a way to register new payloads.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterPayload = channel.unary_unary(
        '/bosdyn.api.PayloadRegistrationService/RegisterPayload',
        request_serializer=bosdyn_dot_api_dot_payload__registration__pb2.RegisterPayloadRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_payload__registration__pb2.RegisterPayloadResponse.FromString,
        )
    self.UpdatePayloadVersion = channel.unary_unary(
        '/bosdyn.api.PayloadRegistrationService/UpdatePayloadVersion',
        request_serializer=bosdyn_dot_api_dot_payload__registration__pb2.UpdatePayloadVersionRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_payload__registration__pb2.UpdatePayloadVersionResponse.FromString,
        )
    self.GetPayloadAuthToken = channel.unary_unary(
        '/bosdyn.api.PayloadRegistrationService/GetPayloadAuthToken',
        request_serializer=bosdyn_dot_api_dot_payload__registration__pb2.GetPayloadAuthTokenRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_payload__registration__pb2.GetPayloadAuthTokenResponse.FromString,
        )
    self.UpdatePayloadAttached = channel.unary_unary(
        '/bosdyn.api.PayloadRegistrationService/UpdatePayloadAttached',
        request_serializer=bosdyn_dot_api_dot_payload__registration__pb2.UpdatePayloadAttachedRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_payload__registration__pb2.UpdatePayloadAttachedResponse.FromString,
        )


class PayloadRegistrationServiceServicer(object):
  """This service provides a way to register new payloads.
  """

  def RegisterPayload(self, request, context):
    """Register a payload with the directory.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdatePayloadVersion(self, request, context):
    """Update the version for the registered payload.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPayloadAuthToken(self, request, context):
    """Get the authentication token information associated with a given payload.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdatePayloadAttached(self, request, context):
    """Tell the robot whether the specified payload is attached..
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PayloadRegistrationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterPayload': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterPayload,
          request_deserializer=bosdyn_dot_api_dot_payload__registration__pb2.RegisterPayloadRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_payload__registration__pb2.RegisterPayloadResponse.SerializeToString,
      ),
      'UpdatePayloadVersion': grpc.unary_unary_rpc_method_handler(
          servicer.UpdatePayloadVersion,
          request_deserializer=bosdyn_dot_api_dot_payload__registration__pb2.UpdatePayloadVersionRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_payload__registration__pb2.UpdatePayloadVersionResponse.SerializeToString,
      ),
      'GetPayloadAuthToken': grpc.unary_unary_rpc_method_handler(
          servicer.GetPayloadAuthToken,
          request_deserializer=bosdyn_dot_api_dot_payload__registration__pb2.GetPayloadAuthTokenRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_payload__registration__pb2.GetPayloadAuthTokenResponse.SerializeToString,
      ),
      'UpdatePayloadAttached': grpc.unary_unary_rpc_method_handler(
          servicer.UpdatePayloadAttached,
          request_deserializer=bosdyn_dot_api_dot_payload__registration__pb2.UpdatePayloadAttachedRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_payload__registration__pb2.UpdatePayloadAttachedResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bosdyn.api.PayloadRegistrationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
