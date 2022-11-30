# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import finger_pb2 as finger__pb2


class FingerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Scan = channel.unary_unary(
        '/finger.Finger/Scan',
        request_serializer=finger__pb2.ScanRequest.SerializeToString,
        response_deserializer=finger__pb2.ScanResponse.FromString,
        )
    self.GetImage = channel.unary_unary(
        '/finger.Finger/GetImage',
        request_serializer=finger__pb2.GetImageRequest.SerializeToString,
        response_deserializer=finger__pb2.GetImageResponse.FromString,
        )
    self.Verify = channel.unary_unary(
        '/finger.Finger/Verify',
        request_serializer=finger__pb2.VerifyRequest.SerializeToString,
        response_deserializer=finger__pb2.VerifyResponse.FromString,
        )
    self.GetConfig = channel.unary_unary(
        '/finger.Finger/GetConfig',
        request_serializer=finger__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=finger__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/finger.Finger/SetConfig',
        request_serializer=finger__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=finger__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/finger.Finger/SetConfigMulti',
        request_serializer=finger__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=finger__pb2.SetConfigMultiResponse.FromString,
        )


class FingerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Scan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Verify(self, request, context):
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


def add_FingerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Scan': grpc.unary_unary_rpc_method_handler(
          servicer.Scan,
          request_deserializer=finger__pb2.ScanRequest.FromString,
          response_serializer=finger__pb2.ScanResponse.SerializeToString,
      ),
      'GetImage': grpc.unary_unary_rpc_method_handler(
          servicer.GetImage,
          request_deserializer=finger__pb2.GetImageRequest.FromString,
          response_serializer=finger__pb2.GetImageResponse.SerializeToString,
      ),
      'Verify': grpc.unary_unary_rpc_method_handler(
          servicer.Verify,
          request_deserializer=finger__pb2.VerifyRequest.FromString,
          response_serializer=finger__pb2.VerifyResponse.SerializeToString,
      ),
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=finger__pb2.GetConfigRequest.FromString,
          response_serializer=finger__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=finger__pb2.SetConfigRequest.FromString,
          response_serializer=finger__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=finger__pb2.SetConfigMultiRequest.FromString,
          response_serializer=finger__pb2.SetConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'finger.Finger', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
