# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from grid.protos.grid.v1 import whoami_pb2 as grid_dot_v1_dot_whoami__pb2


class AuthenticationServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.WhoAmI = channel.unary_unary(
        '/grid.v1.AuthenticationService/WhoAmI',
        request_serializer=grid_dot_v1_dot_whoami__pb2.WhoAmIRequest.SerializeToString,
        response_deserializer=grid_dot_v1_dot_whoami__pb2.WhoAmIResponse.FromString,
        )


class AuthenticationServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def WhoAmI(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthenticationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'WhoAmI': grpc.unary_unary_rpc_method_handler(
          servicer.WhoAmI,
          request_deserializer=grid_dot_v1_dot_whoami__pb2.WhoAmIRequest.FromString,
          response_serializer=grid_dot_v1_dot_whoami__pb2.WhoAmIResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grid.v1.AuthenticationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
