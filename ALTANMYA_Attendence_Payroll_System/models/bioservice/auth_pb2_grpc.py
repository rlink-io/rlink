# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import auth_pb2 as auth__pb2


class AuthStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfig = channel.unary_unary(
        '/auth.Auth/GetConfig',
        request_serializer=auth__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=auth__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/auth.Auth/SetConfig',
        request_serializer=auth__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=auth__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/auth.Auth/SetConfigMulti',
        request_serializer=auth__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=auth__pb2.SetConfigMultiResponse.FromString,
        )


class AuthServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=auth__pb2.GetConfigRequest.FromString,
          response_serializer=auth__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=auth__pb2.SetConfigRequest.FromString,
          response_serializer=auth__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=auth__pb2.SetConfigMultiRequest.FromString,
          response_serializer=auth__pb2.SetConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'auth.Auth', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
