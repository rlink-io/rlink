# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import device_pb2 as device__pb2


class DeviceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetInfo = channel.unary_unary(
        '/device.Device/GetInfo',
        request_serializer=device__pb2.GetInfoRequest.SerializeToString,
        response_deserializer=device__pb2.GetInfoResponse.FromString,
        )
    self.GetCapabilityInfo = channel.unary_unary(
        '/device.Device/GetCapabilityInfo',
        request_serializer=device__pb2.GetCapabilityInfoRequest.SerializeToString,
        response_deserializer=device__pb2.GetCapabilityInfoResponse.FromString,
        )
    self.DeleteRootCA = channel.unary_unary(
        '/device.Device/DeleteRootCA',
        request_serializer=device__pb2.DeleteRootCARequest.SerializeToString,
        response_deserializer=device__pb2.DeleteRootCAResponse.FromString,
        )
    self.Lock = channel.unary_unary(
        '/device.Device/Lock',
        request_serializer=device__pb2.LockRequest.SerializeToString,
        response_deserializer=device__pb2.LockResponse.FromString,
        )
    self.LockMulti = channel.unary_unary(
        '/device.Device/LockMulti',
        request_serializer=device__pb2.LockMultiRequest.SerializeToString,
        response_deserializer=device__pb2.LockMultiResponse.FromString,
        )
    self.Unlock = channel.unary_unary(
        '/device.Device/Unlock',
        request_serializer=device__pb2.UnlockRequest.SerializeToString,
        response_deserializer=device__pb2.UnlockResponse.FromString,
        )
    self.UnlockMulti = channel.unary_unary(
        '/device.Device/UnlockMulti',
        request_serializer=device__pb2.UnlockMultiRequest.SerializeToString,
        response_deserializer=device__pb2.UnlockMultiResponse.FromString,
        )
    self.Reboot = channel.unary_unary(
        '/device.Device/Reboot',
        request_serializer=device__pb2.RebootRequest.SerializeToString,
        response_deserializer=device__pb2.RebootResponse.FromString,
        )
    self.RebootMulti = channel.unary_unary(
        '/device.Device/RebootMulti',
        request_serializer=device__pb2.RebootMultiRequest.SerializeToString,
        response_deserializer=device__pb2.RebootMultiResponse.FromString,
        )
    self.FactoryReset = channel.unary_unary(
        '/device.Device/FactoryReset',
        request_serializer=device__pb2.FactoryResetRequest.SerializeToString,
        response_deserializer=device__pb2.FactoryResetResponse.FromString,
        )
    self.FactoryResetMulti = channel.unary_unary(
        '/device.Device/FactoryResetMulti',
        request_serializer=device__pb2.FactoryResetMultiRequest.SerializeToString,
        response_deserializer=device__pb2.FactoryResetMultiResponse.FromString,
        )
    self.ClearDB = channel.unary_unary(
        '/device.Device/ClearDB',
        request_serializer=device__pb2.ClearDBRequest.SerializeToString,
        response_deserializer=device__pb2.ClearDBResponse.FromString,
        )
    self.ClearDBMulti = channel.unary_unary(
        '/device.Device/ClearDBMulti',
        request_serializer=device__pb2.ClearDBMultiRequest.SerializeToString,
        response_deserializer=device__pb2.ClearDBMultiResponse.FromString,
        )
    self.ResetConfig = channel.unary_unary(
        '/device.Device/ResetConfig',
        request_serializer=device__pb2.ResetConfigRequest.SerializeToString,
        response_deserializer=device__pb2.ResetConfigResponse.FromString,
        )
    self.ResetConfigMulti = channel.unary_unary(
        '/device.Device/ResetConfigMulti',
        request_serializer=device__pb2.ResetConfigMultiRequest.SerializeToString,
        response_deserializer=device__pb2.ResetConfigMultiResponse.FromString,
        )
    self.UpgradeFirmware = channel.unary_unary(
        '/device.Device/UpgradeFirmware',
        request_serializer=device__pb2.UpgradeFirmwareRequest.SerializeToString,
        response_deserializer=device__pb2.UpgradeFirmwareResponse.FromString,
        )
    self.UpgradeFirmwareMulti = channel.unary_unary(
        '/device.Device/UpgradeFirmwareMulti',
        request_serializer=device__pb2.UpgradeFirmwareMultiRequest.SerializeToString,
        response_deserializer=device__pb2.UpgradeFirmwareMultiResponse.FromString,
        )
    self.GetHashKey = channel.unary_unary(
        '/device.Device/GetHashKey',
        request_serializer=device__pb2.GetHashKeyRequest.SerializeToString,
        response_deserializer=device__pb2.GetHashKeyResponse.FromString,
        )
    self.SetHashKey = channel.unary_unary(
        '/device.Device/SetHashKey',
        request_serializer=device__pb2.SetHashKeyRequest.SerializeToString,
        response_deserializer=device__pb2.SetHashKeyResponse.FromString,
        )


class DeviceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCapabilityInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteRootCA(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Lock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LockMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Unlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnlockMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Reboot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RebootMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FactoryReset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FactoryResetMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClearDB(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClearDBMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpgradeFirmware(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpgradeFirmwareMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetHashKey(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetHashKey(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DeviceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetInfo,
          request_deserializer=device__pb2.GetInfoRequest.FromString,
          response_serializer=device__pb2.GetInfoResponse.SerializeToString,
      ),
      'GetCapabilityInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetCapabilityInfo,
          request_deserializer=device__pb2.GetCapabilityInfoRequest.FromString,
          response_serializer=device__pb2.GetCapabilityInfoResponse.SerializeToString,
      ),
      'DeleteRootCA': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteRootCA,
          request_deserializer=device__pb2.DeleteRootCARequest.FromString,
          response_serializer=device__pb2.DeleteRootCAResponse.SerializeToString,
      ),
      'Lock': grpc.unary_unary_rpc_method_handler(
          servicer.Lock,
          request_deserializer=device__pb2.LockRequest.FromString,
          response_serializer=device__pb2.LockResponse.SerializeToString,
      ),
      'LockMulti': grpc.unary_unary_rpc_method_handler(
          servicer.LockMulti,
          request_deserializer=device__pb2.LockMultiRequest.FromString,
          response_serializer=device__pb2.LockMultiResponse.SerializeToString,
      ),
      'Unlock': grpc.unary_unary_rpc_method_handler(
          servicer.Unlock,
          request_deserializer=device__pb2.UnlockRequest.FromString,
          response_serializer=device__pb2.UnlockResponse.SerializeToString,
      ),
      'UnlockMulti': grpc.unary_unary_rpc_method_handler(
          servicer.UnlockMulti,
          request_deserializer=device__pb2.UnlockMultiRequest.FromString,
          response_serializer=device__pb2.UnlockMultiResponse.SerializeToString,
      ),
      'Reboot': grpc.unary_unary_rpc_method_handler(
          servicer.Reboot,
          request_deserializer=device__pb2.RebootRequest.FromString,
          response_serializer=device__pb2.RebootResponse.SerializeToString,
      ),
      'RebootMulti': grpc.unary_unary_rpc_method_handler(
          servicer.RebootMulti,
          request_deserializer=device__pb2.RebootMultiRequest.FromString,
          response_serializer=device__pb2.RebootMultiResponse.SerializeToString,
      ),
      'FactoryReset': grpc.unary_unary_rpc_method_handler(
          servicer.FactoryReset,
          request_deserializer=device__pb2.FactoryResetRequest.FromString,
          response_serializer=device__pb2.FactoryResetResponse.SerializeToString,
      ),
      'FactoryResetMulti': grpc.unary_unary_rpc_method_handler(
          servicer.FactoryResetMulti,
          request_deserializer=device__pb2.FactoryResetMultiRequest.FromString,
          response_serializer=device__pb2.FactoryResetMultiResponse.SerializeToString,
      ),
      'ClearDB': grpc.unary_unary_rpc_method_handler(
          servicer.ClearDB,
          request_deserializer=device__pb2.ClearDBRequest.FromString,
          response_serializer=device__pb2.ClearDBResponse.SerializeToString,
      ),
      'ClearDBMulti': grpc.unary_unary_rpc_method_handler(
          servicer.ClearDBMulti,
          request_deserializer=device__pb2.ClearDBMultiRequest.FromString,
          response_serializer=device__pb2.ClearDBMultiResponse.SerializeToString,
      ),
      'ResetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.ResetConfig,
          request_deserializer=device__pb2.ResetConfigRequest.FromString,
          response_serializer=device__pb2.ResetConfigResponse.SerializeToString,
      ),
      'ResetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.ResetConfigMulti,
          request_deserializer=device__pb2.ResetConfigMultiRequest.FromString,
          response_serializer=device__pb2.ResetConfigMultiResponse.SerializeToString,
      ),
      'UpgradeFirmware': grpc.unary_unary_rpc_method_handler(
          servicer.UpgradeFirmware,
          request_deserializer=device__pb2.UpgradeFirmwareRequest.FromString,
          response_serializer=device__pb2.UpgradeFirmwareResponse.SerializeToString,
      ),
      'UpgradeFirmwareMulti': grpc.unary_unary_rpc_method_handler(
          servicer.UpgradeFirmwareMulti,
          request_deserializer=device__pb2.UpgradeFirmwareMultiRequest.FromString,
          response_serializer=device__pb2.UpgradeFirmwareMultiResponse.SerializeToString,
      ),
      'GetHashKey': grpc.unary_unary_rpc_method_handler(
          servicer.GetHashKey,
          request_deserializer=device__pb2.GetHashKeyRequest.FromString,
          response_serializer=device__pb2.GetHashKeyResponse.SerializeToString,
      ),
      'SetHashKey': grpc.unary_unary_rpc_method_handler(
          servicer.SetHashKey,
          request_deserializer=device__pb2.SetHashKeyRequest.FromString,
          response_serializer=device__pb2.SetHashKeyResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'device.Device', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
