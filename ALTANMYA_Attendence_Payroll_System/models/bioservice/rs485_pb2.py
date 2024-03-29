# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rs485.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import device_pb2 as device__pb2
import err_pb2 as err__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rs485.proto',
  package='rs485',
  syntax='proto3',
  serialized_options=_b('\n\030com.supremainc.sdk.rs485P\001Z\025biostar/service/rs485'),
  serialized_pb=_b('\n\x0brs485.proto\x12\x05rs485\x1a\x0c\x64\x65vice.proto\x1a\terr.proto\"v\n\x0fSlaveDeviceInfo\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x1a\n\x04type\x18\x02 \x01(\x0e\x32\x0c.device.Type\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x11\n\tconnected\x18\x04 \x01(\x08\x12\x11\n\tchannelID\x18\x05 \x01(\r\"\'\n\x13SearchDeviceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"B\n\x14SearchDeviceResponse\x12*\n\nslaveInfos\x18\x01 \x03(\x0b\x32\x16.rs485.SlaveDeviceInfo\"P\n\x10SetDeviceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12*\n\nslaveInfos\x18\x02 \x03(\x0b\x32\x16.rs485.SlaveDeviceInfo\"\x13\n\x11SetDeviceResponse\"$\n\x10GetDeviceRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"?\n\x11GetDeviceResponse\x12*\n\nslaveInfos\x18\x02 \x03(\x0b\x32\x16.rs485.SlaveDeviceInfo\"\x82\x01\n\x11IntelligentPDInfo\x12\x18\n\x10useExceptionCode\x18\x01 \x01(\x08\x12\x15\n\rexceptionCode\x18\x02 \x01(\x0c\x12,\n\x0coutputFormat\x18\x03 \x01(\x0e\x32\x16.rs485.IPDOutputFormat\x12\x0e\n\x06OSDPID\x18\x04 \x01(\r\"N\n\x0cRS485Channel\x12\x11\n\tchannelID\x18\x01 \x01(\r\x12\x19\n\x04mode\x18\x02 \x01(\x0e\x32\x0b.rs485.Mode\x12\x10\n\x08\x62\x61udRate\x18\x03 \x01(\r\"g\n\x0bRS485Config\x12%\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x13.rs485.RS485Channel\x12\x31\n\x0fintelligentInfo\x18\x02 \x01(\x0b\x32\x18.rs485.IntelligentPDInfo\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\"7\n\x11GetConfigResponse\x12\"\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x12.rs485.RS485Config\"H\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\"\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x12.rs485.RS485Config\"\x13\n\x11SetConfigResponse\"N\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12\"\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x12.rs485.RS485Config\"B\n\x16SetConfigMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse*:\n\x04Mode\x12\x0b\n\x07NOT_USE\x10\x00\x12\n\n\x06MASTER\x10\x01\x12\t\n\x05SLAVE\x10\x02\x12\x0e\n\nSTANDALONE\x10\x03*)\n\x0fIPDOutputFormat\x12\n\n\x06\x43\x41RDID\x10\x00\x12\n\n\x06USERID\x10\x01\x32\x9f\x03\n\x05RS485\x12G\n\x0cSearchDevice\x12\x1a.rs485.SearchDeviceRequest\x1a\x1b.rs485.SearchDeviceResponse\x12>\n\tGetDevice\x12\x17.rs485.GetDeviceRequest\x1a\x18.rs485.GetDeviceResponse\x12>\n\tSetDevice\x12\x17.rs485.SetDeviceRequest\x1a\x18.rs485.SetDeviceResponse\x12>\n\tGetConfig\x12\x17.rs485.GetConfigRequest\x1a\x18.rs485.GetConfigResponse\x12>\n\tSetConfig\x12\x17.rs485.SetConfigRequest\x1a\x18.rs485.SetConfigResponse\x12M\n\x0eSetConfigMulti\x12\x1c.rs485.SetConfigMultiRequest\x1a\x1d.rs485.SetConfigMultiResponseB3\n\x18\x63om.supremainc.sdk.rs485P\x01Z\x15\x62iostar/service/rs485b\x06proto3')
  ,
  dependencies=[device__pb2.DESCRIPTOR,err__pb2.DESCRIPTOR,])

_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='rs485.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_USE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MASTER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLAVE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STANDALONE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1138,
  serialized_end=1196,
)
_sym_db.RegisterEnumDescriptor(_MODE)

Mode = enum_type_wrapper.EnumTypeWrapper(_MODE)
_IPDOUTPUTFORMAT = _descriptor.EnumDescriptor(
  name='IPDOutputFormat',
  full_name='rs485.IPDOutputFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CARDID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERID', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1198,
  serialized_end=1239,
)
_sym_db.RegisterEnumDescriptor(_IPDOUTPUTFORMAT)

IPDOutputFormat = enum_type_wrapper.EnumTypeWrapper(_IPDOUTPUTFORMAT)
NOT_USE = 0
MASTER = 1
SLAVE = 2
STANDALONE = 3
CARDID = 0
USERID = 1



_SLAVEDEVICEINFO = _descriptor.Descriptor(
  name='SlaveDeviceInfo',
  full_name='rs485.SlaveDeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='rs485.SlaveDeviceInfo.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='rs485.SlaveDeviceInfo.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='rs485.SlaveDeviceInfo.enabled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connected', full_name='rs485.SlaveDeviceInfo.connected', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channelID', full_name='rs485.SlaveDeviceInfo.channelID', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=47,
  serialized_end=165,
)


_SEARCHDEVICEREQUEST = _descriptor.Descriptor(
  name='SearchDeviceRequest',
  full_name='rs485.SearchDeviceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='rs485.SearchDeviceRequest.deviceID', index=0,
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
  serialized_start=167,
  serialized_end=206,
)


_SEARCHDEVICERESPONSE = _descriptor.Descriptor(
  name='SearchDeviceResponse',
  full_name='rs485.SearchDeviceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slaveInfos', full_name='rs485.SearchDeviceResponse.slaveInfos', index=0,
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
  serialized_start=208,
  serialized_end=274,
)


_SETDEVICEREQUEST = _descriptor.Descriptor(
  name='SetDeviceRequest',
  full_name='rs485.SetDeviceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='rs485.SetDeviceRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slaveInfos', full_name='rs485.SetDeviceRequest.slaveInfos', index=1,
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
  serialized_start=276,
  serialized_end=356,
)


_SETDEVICERESPONSE = _descriptor.Descriptor(
  name='SetDeviceResponse',
  full_name='rs485.SetDeviceResponse',
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
  serialized_start=358,
  serialized_end=377,
)


_GETDEVICEREQUEST = _descriptor.Descriptor(
  name='GetDeviceRequest',
  full_name='rs485.GetDeviceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='rs485.GetDeviceRequest.deviceID', index=0,
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
  serialized_start=379,
  serialized_end=415,
)


_GETDEVICERESPONSE = _descriptor.Descriptor(
  name='GetDeviceResponse',
  full_name='rs485.GetDeviceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slaveInfos', full_name='rs485.GetDeviceResponse.slaveInfos', index=0,
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
  serialized_start=417,
  serialized_end=480,
)


_INTELLIGENTPDINFO = _descriptor.Descriptor(
  name='IntelligentPDInfo',
  full_name='rs485.IntelligentPDInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='useExceptionCode', full_name='rs485.IntelligentPDInfo.useExceptionCode', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exceptionCode', full_name='rs485.IntelligentPDInfo.exceptionCode', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputFormat', full_name='rs485.IntelligentPDInfo.outputFormat', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='OSDPID', full_name='rs485.IntelligentPDInfo.OSDPID', index=3,
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
  serialized_start=483,
  serialized_end=613,
)


_RS485CHANNEL = _descriptor.Descriptor(
  name='RS485Channel',
  full_name='rs485.RS485Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelID', full_name='rs485.RS485Channel.channelID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='rs485.RS485Channel.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='baudRate', full_name='rs485.RS485Channel.baudRate', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=615,
  serialized_end=693,
)


_RS485CONFIG = _descriptor.Descriptor(
  name='RS485Config',
  full_name='rs485.RS485Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='rs485.RS485Config.channels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intelligentInfo', full_name='rs485.RS485Config.intelligentInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=695,
  serialized_end=798,
)


_GETCONFIGREQUEST = _descriptor.Descriptor(
  name='GetConfigRequest',
  full_name='rs485.GetConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='rs485.GetConfigRequest.deviceID', index=0,
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
  serialized_start=800,
  serialized_end=836,
)


_GETCONFIGRESPONSE = _descriptor.Descriptor(
  name='GetConfigResponse',
  full_name='rs485.GetConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='rs485.GetConfigResponse.config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=838,
  serialized_end=893,
)


_SETCONFIGREQUEST = _descriptor.Descriptor(
  name='SetConfigRequest',
  full_name='rs485.SetConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='rs485.SetConfigRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='rs485.SetConfigRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=895,
  serialized_end=967,
)


_SETCONFIGRESPONSE = _descriptor.Descriptor(
  name='SetConfigResponse',
  full_name='rs485.SetConfigResponse',
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
  serialized_start=969,
  serialized_end=988,
)


_SETCONFIGMULTIREQUEST = _descriptor.Descriptor(
  name='SetConfigMultiRequest',
  full_name='rs485.SetConfigMultiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceIDs', full_name='rs485.SetConfigMultiRequest.deviceIDs', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='rs485.SetConfigMultiRequest.config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=990,
  serialized_end=1068,
)


_SETCONFIGMULTIRESPONSE = _descriptor.Descriptor(
  name='SetConfigMultiResponse',
  full_name='rs485.SetConfigMultiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceErrors', full_name='rs485.SetConfigMultiResponse.deviceErrors', index=0,
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
  serialized_start=1070,
  serialized_end=1136,
)

_SLAVEDEVICEINFO.fields_by_name['type'].enum_type = device__pb2._TYPE
_SEARCHDEVICERESPONSE.fields_by_name['slaveInfos'].message_type = _SLAVEDEVICEINFO
_SETDEVICEREQUEST.fields_by_name['slaveInfos'].message_type = _SLAVEDEVICEINFO
_GETDEVICERESPONSE.fields_by_name['slaveInfos'].message_type = _SLAVEDEVICEINFO
_INTELLIGENTPDINFO.fields_by_name['outputFormat'].enum_type = _IPDOUTPUTFORMAT
_RS485CHANNEL.fields_by_name['mode'].enum_type = _MODE
_RS485CONFIG.fields_by_name['channels'].message_type = _RS485CHANNEL
_RS485CONFIG.fields_by_name['intelligentInfo'].message_type = _INTELLIGENTPDINFO
_GETCONFIGRESPONSE.fields_by_name['config'].message_type = _RS485CONFIG
_SETCONFIGREQUEST.fields_by_name['config'].message_type = _RS485CONFIG
_SETCONFIGMULTIREQUEST.fields_by_name['config'].message_type = _RS485CONFIG
_SETCONFIGMULTIRESPONSE.fields_by_name['deviceErrors'].message_type = err__pb2._ERRORRESPONSE
DESCRIPTOR.message_types_by_name['SlaveDeviceInfo'] = _SLAVEDEVICEINFO
DESCRIPTOR.message_types_by_name['SearchDeviceRequest'] = _SEARCHDEVICEREQUEST
DESCRIPTOR.message_types_by_name['SearchDeviceResponse'] = _SEARCHDEVICERESPONSE
DESCRIPTOR.message_types_by_name['SetDeviceRequest'] = _SETDEVICEREQUEST
DESCRIPTOR.message_types_by_name['SetDeviceResponse'] = _SETDEVICERESPONSE
DESCRIPTOR.message_types_by_name['GetDeviceRequest'] = _GETDEVICEREQUEST
DESCRIPTOR.message_types_by_name['GetDeviceResponse'] = _GETDEVICERESPONSE
DESCRIPTOR.message_types_by_name['IntelligentPDInfo'] = _INTELLIGENTPDINFO
DESCRIPTOR.message_types_by_name['RS485Channel'] = _RS485CHANNEL
DESCRIPTOR.message_types_by_name['RS485Config'] = _RS485CONFIG
DESCRIPTOR.message_types_by_name['GetConfigRequest'] = _GETCONFIGREQUEST
DESCRIPTOR.message_types_by_name['GetConfigResponse'] = _GETCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['SetConfigRequest'] = _SETCONFIGREQUEST
DESCRIPTOR.message_types_by_name['SetConfigResponse'] = _SETCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['SetConfigMultiRequest'] = _SETCONFIGMULTIREQUEST
DESCRIPTOR.message_types_by_name['SetConfigMultiResponse'] = _SETCONFIGMULTIRESPONSE
DESCRIPTOR.enum_types_by_name['Mode'] = _MODE
DESCRIPTOR.enum_types_by_name['IPDOutputFormat'] = _IPDOUTPUTFORMAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SlaveDeviceInfo = _reflection.GeneratedProtocolMessageType('SlaveDeviceInfo', (_message.Message,), dict(
  DESCRIPTOR = _SLAVEDEVICEINFO,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SlaveDeviceInfo)
  ))
_sym_db.RegisterMessage(SlaveDeviceInfo)

SearchDeviceRequest = _reflection.GeneratedProtocolMessageType('SearchDeviceRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHDEVICEREQUEST,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SearchDeviceRequest)
  ))
_sym_db.RegisterMessage(SearchDeviceRequest)

SearchDeviceResponse = _reflection.GeneratedProtocolMessageType('SearchDeviceResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHDEVICERESPONSE,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SearchDeviceResponse)
  ))
_sym_db.RegisterMessage(SearchDeviceResponse)

SetDeviceRequest = _reflection.GeneratedProtocolMessageType('SetDeviceRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETDEVICEREQUEST,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SetDeviceRequest)
  ))
_sym_db.RegisterMessage(SetDeviceRequest)

SetDeviceResponse = _reflection.GeneratedProtocolMessageType('SetDeviceResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETDEVICERESPONSE,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SetDeviceResponse)
  ))
_sym_db.RegisterMessage(SetDeviceResponse)

GetDeviceRequest = _reflection.GeneratedProtocolMessageType('GetDeviceRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETDEVICEREQUEST,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.GetDeviceRequest)
  ))
_sym_db.RegisterMessage(GetDeviceRequest)

GetDeviceResponse = _reflection.GeneratedProtocolMessageType('GetDeviceResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETDEVICERESPONSE,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.GetDeviceResponse)
  ))
_sym_db.RegisterMessage(GetDeviceResponse)

IntelligentPDInfo = _reflection.GeneratedProtocolMessageType('IntelligentPDInfo', (_message.Message,), dict(
  DESCRIPTOR = _INTELLIGENTPDINFO,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.IntelligentPDInfo)
  ))
_sym_db.RegisterMessage(IntelligentPDInfo)

RS485Channel = _reflection.GeneratedProtocolMessageType('RS485Channel', (_message.Message,), dict(
  DESCRIPTOR = _RS485CHANNEL,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.RS485Channel)
  ))
_sym_db.RegisterMessage(RS485Channel)

RS485Config = _reflection.GeneratedProtocolMessageType('RS485Config', (_message.Message,), dict(
  DESCRIPTOR = _RS485CONFIG,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.RS485Config)
  ))
_sym_db.RegisterMessage(RS485Config)

GetConfigRequest = _reflection.GeneratedProtocolMessageType('GetConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGREQUEST,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.GetConfigRequest)
  ))
_sym_db.RegisterMessage(GetConfigRequest)

GetConfigResponse = _reflection.GeneratedProtocolMessageType('GetConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGRESPONSE,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.GetConfigResponse)
  ))
_sym_db.RegisterMessage(GetConfigResponse)

SetConfigRequest = _reflection.GeneratedProtocolMessageType('SetConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGREQUEST,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SetConfigRequest)
  ))
_sym_db.RegisterMessage(SetConfigRequest)

SetConfigResponse = _reflection.GeneratedProtocolMessageType('SetConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGRESPONSE,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SetConfigResponse)
  ))
_sym_db.RegisterMessage(SetConfigResponse)

SetConfigMultiRequest = _reflection.GeneratedProtocolMessageType('SetConfigMultiRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGMULTIREQUEST,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SetConfigMultiRequest)
  ))
_sym_db.RegisterMessage(SetConfigMultiRequest)

SetConfigMultiResponse = _reflection.GeneratedProtocolMessageType('SetConfigMultiResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGMULTIRESPONSE,
  __module__ = 'rs485_pb2'
  # @@protoc_insertion_point(class_scope:rs485.SetConfigMultiResponse)
  ))
_sym_db.RegisterMessage(SetConfigMultiResponse)


DESCRIPTOR._options = None

_RS485 = _descriptor.ServiceDescriptor(
  name='RS485',
  full_name='rs485.RS485',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1242,
  serialized_end=1657,
  methods=[
  _descriptor.MethodDescriptor(
    name='SearchDevice',
    full_name='rs485.RS485.SearchDevice',
    index=0,
    containing_service=None,
    input_type=_SEARCHDEVICEREQUEST,
    output_type=_SEARCHDEVICERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDevice',
    full_name='rs485.RS485.GetDevice',
    index=1,
    containing_service=None,
    input_type=_GETDEVICEREQUEST,
    output_type=_GETDEVICERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetDevice',
    full_name='rs485.RS485.SetDevice',
    index=2,
    containing_service=None,
    input_type=_SETDEVICEREQUEST,
    output_type=_SETDEVICERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetConfig',
    full_name='rs485.RS485.GetConfig',
    index=3,
    containing_service=None,
    input_type=_GETCONFIGREQUEST,
    output_type=_GETCONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetConfig',
    full_name='rs485.RS485.SetConfig',
    index=4,
    containing_service=None,
    input_type=_SETCONFIGREQUEST,
    output_type=_SETCONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetConfigMulti',
    full_name='rs485.RS485.SetConfigMulti',
    index=5,
    containing_service=None,
    input_type=_SETCONFIGMULTIREQUEST,
    output_type=_SETCONFIGMULTIRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RS485)

DESCRIPTOR.services_by_name['RS485'] = _RS485

# @@protoc_insertion_point(module_scope)
