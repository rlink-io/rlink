# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fire_zone.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import zone_pb2 as zone__pb2
import action_pb2 as action__pb2
import device_pb2 as device__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fire_zone.proto',
  package='fire_zone',
  syntax='proto3',
  serialized_options=_b('\n\034com.supremainc.sdk.fire_zoneP\001Z\030biostar/service/fireZone'),
  serialized_pb=_b('\n\x0f\x66ire_zone.proto\x12\tfire_zone\x1a\nzone.proto\x1a\x0c\x61\x63tion.proto\x1a\x0c\x64\x65vice.proto\"`\n\nFireSensor\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\x12 \n\x04type\x18\x03 \x01(\x0e\x32\x12.device.SwitchType\x12\x10\n\x08\x64uration\x18\x04 \x01(\r\"\xa5\x01\n\x08ZoneInfo\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08\x12\x0f\n\x07\x61larmed\x18\x04 \x01(\x08\x12\x0f\n\x07\x64oorIDs\x18\x05 \x03(\r\x12&\n\x07sensors\x18\x06 \x03(\x0b\x32\x15.fire_zone.FireSensor\x12\x1f\n\x07\x61\x63tions\x18\x07 \x03(\x0b\x32\x0e.action.Action\"\x1e\n\nGetRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"1\n\x0bGetResponse\x12\"\n\x05zones\x18\x01 \x03(\x0b\x32\x13.fire_zone.ZoneInfo\"5\n\x10GetStatusRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\"5\n\x11GetStatusResponse\x12 \n\x06status\x18\x01 \x03(\x0b\x32\x10.zone.ZoneStatus\"B\n\nAddRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\"\n\x05zones\x18\x02 \x03(\x0b\x32\x13.fire_zone.ZoneInfo\"\r\n\x0b\x41\x64\x64Response\"2\n\rDeleteRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\"\x10\n\x0e\x44\x65leteResponse\"$\n\x10\x44\x65leteAllRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"\x13\n\x11\x44\x65leteAllResponse\"E\n\x0fSetAlarmRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x0f\n\x07zoneIDs\x18\x02 \x03(\r\x12\x0f\n\x07\x61larmed\x18\x03 \x01(\x08\"\x12\n\x10SetAlarmResponse2\x8f\x03\n\rFireAlarmZone\x12\x34\n\x03Get\x12\x15.fire_zone.GetRequest\x1a\x16.fire_zone.GetResponse\x12\x46\n\tGetStatus\x12\x1b.fire_zone.GetStatusRequest\x1a\x1c.fire_zone.GetStatusResponse\x12\x34\n\x03\x41\x64\x64\x12\x15.fire_zone.AddRequest\x1a\x16.fire_zone.AddResponse\x12=\n\x06\x44\x65lete\x12\x18.fire_zone.DeleteRequest\x1a\x19.fire_zone.DeleteResponse\x12\x46\n\tDeleteAll\x12\x1b.fire_zone.DeleteAllRequest\x1a\x1c.fire_zone.DeleteAllResponse\x12\x43\n\x08SetAlarm\x12\x1a.fire_zone.SetAlarmRequest\x1a\x1b.fire_zone.SetAlarmResponseB:\n\x1c\x63om.supremainc.sdk.fire_zoneP\x01Z\x18\x62iostar/service/fireZoneb\x06proto3')
  ,
  dependencies=[zone__pb2.DESCRIPTOR,action__pb2.DESCRIPTOR,device__pb2.DESCRIPTOR,])




_FIRESENSOR = _descriptor.Descriptor(
  name='FireSensor',
  full_name='fire_zone.FireSensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='fire_zone.FireSensor.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='fire_zone.FireSensor.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='fire_zone.FireSensor.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='fire_zone.FireSensor.duration', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=166,
)


_ZONEINFO = _descriptor.Descriptor(
  name='ZoneInfo',
  full_name='fire_zone.ZoneInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zoneID', full_name='fire_zone.ZoneInfo.zoneID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='fire_zone.ZoneInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='fire_zone.ZoneInfo.disabled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alarmed', full_name='fire_zone.ZoneInfo.alarmed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='doorIDs', full_name='fire_zone.ZoneInfo.doorIDs', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sensors', full_name='fire_zone.ZoneInfo.sensors', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='fire_zone.ZoneInfo.actions', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=334,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='fire_zone.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='fire_zone.GetRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=366,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='fire_zone.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zones', full_name='fire_zone.GetResponse.zones', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=417,
)


_GETSTATUSREQUEST = _descriptor.Descriptor(
  name='GetStatusRequest',
  full_name='fire_zone.GetStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='fire_zone.GetStatusRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoneIDs', full_name='fire_zone.GetStatusRequest.zoneIDs', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=419,
  serialized_end=472,
)


_GETSTATUSRESPONSE = _descriptor.Descriptor(
  name='GetStatusResponse',
  full_name='fire_zone.GetStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fire_zone.GetStatusResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=474,
  serialized_end=527,
)


_ADDREQUEST = _descriptor.Descriptor(
  name='AddRequest',
  full_name='fire_zone.AddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='fire_zone.AddRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zones', full_name='fire_zone.AddRequest.zones', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=595,
)


_ADDRESPONSE = _descriptor.Descriptor(
  name='AddResponse',
  full_name='fire_zone.AddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=597,
  serialized_end=610,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='fire_zone.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='fire_zone.DeleteRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoneIDs', full_name='fire_zone.DeleteRequest.zoneIDs', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=612,
  serialized_end=662,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='fire_zone.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=664,
  serialized_end=680,
)


_DELETEALLREQUEST = _descriptor.Descriptor(
  name='DeleteAllRequest',
  full_name='fire_zone.DeleteAllRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='fire_zone.DeleteAllRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=718,
)


_DELETEALLRESPONSE = _descriptor.Descriptor(
  name='DeleteAllResponse',
  full_name='fire_zone.DeleteAllResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=720,
  serialized_end=739,
)


_SETALARMREQUEST = _descriptor.Descriptor(
  name='SetAlarmRequest',
  full_name='fire_zone.SetAlarmRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='fire_zone.SetAlarmRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zoneIDs', full_name='fire_zone.SetAlarmRequest.zoneIDs', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alarmed', full_name='fire_zone.SetAlarmRequest.alarmed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=810,
)


_SETALARMRESPONSE = _descriptor.Descriptor(
  name='SetAlarmResponse',
  full_name='fire_zone.SetAlarmResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=812,
  serialized_end=830,
)

_FIRESENSOR.fields_by_name['type'].enum_type = device__pb2._SWITCHTYPE
_ZONEINFO.fields_by_name['sensors'].message_type = _FIRESENSOR
_ZONEINFO.fields_by_name['actions'].message_type = action__pb2._ACTION
_GETRESPONSE.fields_by_name['zones'].message_type = _ZONEINFO
_GETSTATUSRESPONSE.fields_by_name['status'].message_type = zone__pb2._ZONESTATUS
_ADDREQUEST.fields_by_name['zones'].message_type = _ZONEINFO
DESCRIPTOR.message_types_by_name['FireSensor'] = _FIRESENSOR
DESCRIPTOR.message_types_by_name['ZoneInfo'] = _ZONEINFO
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['GetStatusRequest'] = _GETSTATUSREQUEST
DESCRIPTOR.message_types_by_name['GetStatusResponse'] = _GETSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['AddRequest'] = _ADDREQUEST
DESCRIPTOR.message_types_by_name['AddResponse'] = _ADDRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['DeleteAllRequest'] = _DELETEALLREQUEST
DESCRIPTOR.message_types_by_name['DeleteAllResponse'] = _DELETEALLRESPONSE
DESCRIPTOR.message_types_by_name['SetAlarmRequest'] = _SETALARMREQUEST
DESCRIPTOR.message_types_by_name['SetAlarmResponse'] = _SETALARMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FireSensor = _reflection.GeneratedProtocolMessageType('FireSensor', (_message.Message,), dict(
  DESCRIPTOR = _FIRESENSOR,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.FireSensor)
  ))
_sym_db.RegisterMessage(FireSensor)

ZoneInfo = _reflection.GeneratedProtocolMessageType('ZoneInfo', (_message.Message,), dict(
  DESCRIPTOR = _ZONEINFO,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.ZoneInfo)
  ))
_sym_db.RegisterMessage(ZoneInfo)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREQUEST,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.GetRequest)
  ))
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRESPONSE,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.GetResponse)
  ))
_sym_db.RegisterMessage(GetResponse)

GetStatusRequest = _reflection.GeneratedProtocolMessageType('GetStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSTATUSREQUEST,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.GetStatusRequest)
  ))
_sym_db.RegisterMessage(GetStatusRequest)

GetStatusResponse = _reflection.GeneratedProtocolMessageType('GetStatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSTATUSRESPONSE,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.GetStatusResponse)
  ))
_sym_db.RegisterMessage(GetStatusResponse)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDREQUEST,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.AddRequest)
  ))
_sym_db.RegisterMessage(AddRequest)

AddResponse = _reflection.GeneratedProtocolMessageType('AddResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESPONSE,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.AddResponse)
  ))
_sym_db.RegisterMessage(AddResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETERESPONSE,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.DeleteResponse)
  ))
_sym_db.RegisterMessage(DeleteResponse)

DeleteAllRequest = _reflection.GeneratedProtocolMessageType('DeleteAllRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEALLREQUEST,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.DeleteAllRequest)
  ))
_sym_db.RegisterMessage(DeleteAllRequest)

DeleteAllResponse = _reflection.GeneratedProtocolMessageType('DeleteAllResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETEALLRESPONSE,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.DeleteAllResponse)
  ))
_sym_db.RegisterMessage(DeleteAllResponse)

SetAlarmRequest = _reflection.GeneratedProtocolMessageType('SetAlarmRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETALARMREQUEST,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.SetAlarmRequest)
  ))
_sym_db.RegisterMessage(SetAlarmRequest)

SetAlarmResponse = _reflection.GeneratedProtocolMessageType('SetAlarmResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETALARMRESPONSE,
  __module__ = 'fire_zone_pb2'
  # @@protoc_insertion_point(class_scope:fire_zone.SetAlarmResponse)
  ))
_sym_db.RegisterMessage(SetAlarmResponse)


DESCRIPTOR._options = None

_FIREALARMZONE = _descriptor.ServiceDescriptor(
  name='FireAlarmZone',
  full_name='fire_zone.FireAlarmZone',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=833,
  serialized_end=1232,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='fire_zone.FireAlarmZone.Get',
    index=0,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='fire_zone.FireAlarmZone.GetStatus',
    index=1,
    containing_service=None,
    input_type=_GETSTATUSREQUEST,
    output_type=_GETSTATUSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='fire_zone.FireAlarmZone.Add',
    index=2,
    containing_service=None,
    input_type=_ADDREQUEST,
    output_type=_ADDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='fire_zone.FireAlarmZone.Delete',
    index=3,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAll',
    full_name='fire_zone.FireAlarmZone.DeleteAll',
    index=4,
    containing_service=None,
    input_type=_DELETEALLREQUEST,
    output_type=_DELETEALLRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetAlarm',
    full_name='fire_zone.FireAlarmZone.SetAlarm',
    index=5,
    containing_service=None,
    input_type=_SETALARMREQUEST,
    output_type=_SETALARMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FIREALARMZONE)

DESCRIPTOR.services_by_name['FireAlarmZone'] = _FIREALARMZONE

# @@protoc_insertion_point(module_scope)
