<<<<<<< HEAD
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import action_pb2 as action__pb2


class TriggerActionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfig = channel.unary_unary(
        '/action.TriggerAction/GetConfig',
        request_serializer=action__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=action__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/action.TriggerAction/SetConfig',
        request_serializer=action__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=action__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/action.TriggerAction/SetConfigMulti',
        request_serializer=action__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=action__pb2.SetConfigMultiResponse.FromString,
        )


class TriggerActionServicer(object):
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


def add_TriggerActionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=action__pb2.GetConfigRequest.FromString,
          response_serializer=action__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=action__pb2.SetConfigRequest.FromString,
          response_serializer=action__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=action__pb2.SetConfigMultiRequest.FromString,
          response_serializer=action__pb2.SetConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'action.TriggerAction', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
=======
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import action_pb2 as action__pb2


class TriggerActionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfig = channel.unary_unary(
        '/action.TriggerAction/GetConfig',
        request_serializer=action__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=action__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/action.TriggerAction/SetConfig',
        request_serializer=action__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=action__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/action.TriggerAction/SetConfigMulti',
        request_serializer=action__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=action__pb2.SetConfigMultiResponse.FromString,
        )


class TriggerActionServicer(object):
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


def add_TriggerActionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=action__pb2.GetConfigRequest.FromString,
          response_serializer=action__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=action__pb2.SetConfigRequest.FromString,
          response_serializer=action__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=action__pb2.SetConfigMultiRequest.FromString,
          response_serializer=action__pb2.SetConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'action.TriggerAction', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
>>>>>>> HR
