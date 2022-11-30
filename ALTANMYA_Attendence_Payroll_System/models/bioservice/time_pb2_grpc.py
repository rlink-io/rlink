<<<<<<< HEAD
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import time_pb2 as time__pb2


class TimeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/time.Time/Get',
        request_serializer=time__pb2.GetRequest.SerializeToString,
        response_deserializer=time__pb2.GetResponse.FromString,
        )
    self.Set = channel.unary_unary(
        '/time.Time/Set',
        request_serializer=time__pb2.SetRequest.SerializeToString,
        response_deserializer=time__pb2.SetResponse.FromString,
        )
    self.SetMulti = channel.unary_unary(
        '/time.Time/SetMulti',
        request_serializer=time__pb2.SetMultiRequest.SerializeToString,
        response_deserializer=time__pb2.SetMultiResponse.FromString,
        )
    self.GetConfig = channel.unary_unary(
        '/time.Time/GetConfig',
        request_serializer=time__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=time__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/time.Time/SetConfig',
        request_serializer=time__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=time__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/time.Time/SetConfigMulti',
        request_serializer=time__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=time__pb2.SetConfigMultiResponse.FromString,
        )
    self.GetDSTConfig = channel.unary_unary(
        '/time.Time/GetDSTConfig',
        request_serializer=time__pb2.GetDSTConfigRequest.SerializeToString,
        response_deserializer=time__pb2.GetDSTConfigResponse.FromString,
        )
    self.SetDSTConfig = channel.unary_unary(
        '/time.Time/SetDSTConfig',
        request_serializer=time__pb2.SetDSTConfigRequest.SerializeToString,
        response_deserializer=time__pb2.SetDSTConfigResponse.FromString,
        )
    self.SetDSTConfigMulti = channel.unary_unary(
        '/time.Time/SetDSTConfigMulti',
        request_serializer=time__pb2.SetDSTConfigMultiRequest.SerializeToString,
        response_deserializer=time__pb2.SetDSTConfigMultiResponse.FromString,
        )


class TimeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Set(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

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

  def GetDSTConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDSTConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDSTConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TimeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=time__pb2.GetRequest.FromString,
          response_serializer=time__pb2.GetResponse.SerializeToString,
      ),
      'Set': grpc.unary_unary_rpc_method_handler(
          servicer.Set,
          request_deserializer=time__pb2.SetRequest.FromString,
          response_serializer=time__pb2.SetResponse.SerializeToString,
      ),
      'SetMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetMulti,
          request_deserializer=time__pb2.SetMultiRequest.FromString,
          response_serializer=time__pb2.SetMultiResponse.SerializeToString,
      ),
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=time__pb2.GetConfigRequest.FromString,
          response_serializer=time__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=time__pb2.SetConfigRequest.FromString,
          response_serializer=time__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=time__pb2.SetConfigMultiRequest.FromString,
          response_serializer=time__pb2.SetConfigMultiResponse.SerializeToString,
      ),
      'GetDSTConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetDSTConfig,
          request_deserializer=time__pb2.GetDSTConfigRequest.FromString,
          response_serializer=time__pb2.GetDSTConfigResponse.SerializeToString,
      ),
      'SetDSTConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetDSTConfig,
          request_deserializer=time__pb2.SetDSTConfigRequest.FromString,
          response_serializer=time__pb2.SetDSTConfigResponse.SerializeToString,
      ),
      'SetDSTConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetDSTConfigMulti,
          request_deserializer=time__pb2.SetDSTConfigMultiRequest.FromString,
          response_serializer=time__pb2.SetDSTConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'time.Time', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
=======
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import time_pb2 as time__pb2


class TimeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/time.Time/Get',
        request_serializer=time__pb2.GetRequest.SerializeToString,
        response_deserializer=time__pb2.GetResponse.FromString,
        )
    self.Set = channel.unary_unary(
        '/time.Time/Set',
        request_serializer=time__pb2.SetRequest.SerializeToString,
        response_deserializer=time__pb2.SetResponse.FromString,
        )
    self.SetMulti = channel.unary_unary(
        '/time.Time/SetMulti',
        request_serializer=time__pb2.SetMultiRequest.SerializeToString,
        response_deserializer=time__pb2.SetMultiResponse.FromString,
        )
    self.GetConfig = channel.unary_unary(
        '/time.Time/GetConfig',
        request_serializer=time__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=time__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/time.Time/SetConfig',
        request_serializer=time__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=time__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/time.Time/SetConfigMulti',
        request_serializer=time__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=time__pb2.SetConfigMultiResponse.FromString,
        )
    self.GetDSTConfig = channel.unary_unary(
        '/time.Time/GetDSTConfig',
        request_serializer=time__pb2.GetDSTConfigRequest.SerializeToString,
        response_deserializer=time__pb2.GetDSTConfigResponse.FromString,
        )
    self.SetDSTConfig = channel.unary_unary(
        '/time.Time/SetDSTConfig',
        request_serializer=time__pb2.SetDSTConfigRequest.SerializeToString,
        response_deserializer=time__pb2.SetDSTConfigResponse.FromString,
        )
    self.SetDSTConfigMulti = channel.unary_unary(
        '/time.Time/SetDSTConfigMulti',
        request_serializer=time__pb2.SetDSTConfigMultiRequest.SerializeToString,
        response_deserializer=time__pb2.SetDSTConfigMultiResponse.FromString,
        )


class TimeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Set(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

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

  def GetDSTConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDSTConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDSTConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TimeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=time__pb2.GetRequest.FromString,
          response_serializer=time__pb2.GetResponse.SerializeToString,
      ),
      'Set': grpc.unary_unary_rpc_method_handler(
          servicer.Set,
          request_deserializer=time__pb2.SetRequest.FromString,
          response_serializer=time__pb2.SetResponse.SerializeToString,
      ),
      'SetMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetMulti,
          request_deserializer=time__pb2.SetMultiRequest.FromString,
          response_serializer=time__pb2.SetMultiResponse.SerializeToString,
      ),
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=time__pb2.GetConfigRequest.FromString,
          response_serializer=time__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=time__pb2.SetConfigRequest.FromString,
          response_serializer=time__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=time__pb2.SetConfigMultiRequest.FromString,
          response_serializer=time__pb2.SetConfigMultiResponse.SerializeToString,
      ),
      'GetDSTConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetDSTConfig,
          request_deserializer=time__pb2.GetDSTConfigRequest.FromString,
          response_serializer=time__pb2.GetDSTConfigResponse.SerializeToString,
      ),
      'SetDSTConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetDSTConfig,
          request_deserializer=time__pb2.SetDSTConfigRequest.FromString,
          response_serializer=time__pb2.SetDSTConfigResponse.SerializeToString,
      ),
      'SetDSTConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetDSTConfigMulti,
          request_deserializer=time__pb2.SetDSTConfigMultiRequest.FromString,
          response_serializer=time__pb2.SetDSTConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'time.Time', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
>>>>>>> HR
