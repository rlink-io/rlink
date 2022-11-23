# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thermal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import err_pb2 as err__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='thermal.proto',
  package='thermal',
  syntax='proto3',
  serialized_options=_b('\n\032com.supremainc.sdk.thermalP\001Z\027biostar/service/thermal'),
  serialized_pb=_b('\n\rthermal.proto\x12\x07thermal\x1a\terr.proto\"G\n\x10ThermalCameraROI\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\x0e\n\x06height\x18\x04 \x01(\r\"\x9d\x01\n\rThermalCamera\x12\x10\n\x08\x64istance\x18\x01 \x01(\r\x12\x14\n\x0c\x65missionRate\x18\x02 \x01(\r\x12&\n\x03ROI\x18\x03 \x01(\x0b\x32\x19.thermal.ThermalCameraROI\x12\x1b\n\x13useBodyCompensation\x18\x04 \x01(\x08\x12\x1f\n\x17\x63ompensationTemperature\x18\x05 \x01(\x05\"\x8d\x03\n\rThermalConfig\x12%\n\tcheckMode\x18\x01 \x01(\x0e\x32\x12.thermal.CheckMode\x12\'\n\ncheckOrder\x18\x02 \x01(\x0e\x32\x13.thermal.CheckOrder\x12\x35\n\x11temperatureFormat\x18\x03 \x01(\x0e\x32\x1a.thermal.TemperatureFormat\x12\x1c\n\x14temperatureThreshold\x18\x04 \x01(\r\x12\x18\n\x10\x61uditTemperature\x18\x05 \x01(\x08\x12\x16\n\x0euseRejectSound\x18\x06 \x01(\x08\x12\x19\n\x11useOverlapThermal\x18\x07 \x01(\x08\x12&\n\x06\x63\x61mera\x18\x08 \x01(\x0b\x32\x16.thermal.ThermalCamera\x12)\n\rmaskCheckMode\x18\t \x01(\x0e\x32\x12.thermal.CheckMode\x12\x37\n\x12maskDetectionLevel\x18\n \x01(\x0e\x32\x1b.thermal.MaskDetectionLevel\"$\n\x10GetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\";\n\x11GetConfigResponse\x12&\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x16.thermal.ThermalConfig\"L\n\x10SetConfigRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12&\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x16.thermal.ThermalConfig\"\x13\n\x11SetConfigResponse\"R\n\x15SetConfigMultiRequest\x12\x11\n\tdeviceIDs\x18\x01 \x03(\r\x12&\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x16.thermal.ThermalConfig\"B\n\x16SetConfigMultiResponse\x12(\n\x0c\x64\x65viceErrors\x18\x01 \x03(\x0b\x32\x12.err.ErrorResponse\"\x8a\x01\n\x0eTemperatureLog\x12\n\n\x02ID\x18\x01 \x01(\r\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x10\n\x08\x64\x65viceID\x18\x03 \x01(\r\x12\x0e\n\x06userID\x18\x04 \x01(\t\x12\x11\n\teventCode\x18\x05 \x01(\r\x12\x0f\n\x07subCode\x18\x06 \x01(\r\x12\x13\n\x0btemperature\x18\x07 \x01(\r\"W\n\x18GetTemperatureLogRequest\x12\x10\n\x08\x64\x65viceID\x18\x01 \x01(\r\x12\x14\n\x0cstartEventID\x18\x02 \x01(\r\x12\x13\n\x0bmaxNumOfLog\x18\x03 \x01(\r\"O\n\x19GetTemperatureLogResponse\x12\x32\n\x11temperatureEvents\x18\x01 \x03(\x0b\x32\x17.thermal.TemperatureLog*(\n\tCheckMode\x12\x07\n\x03OFF\x10\x00\x12\x08\n\x04HARD\x10\x01\x12\x08\n\x04SOFT\x10\x02*?\n\nCheckOrder\x12\x0e\n\nAFTER_AUTH\x10\x00\x12\x0f\n\x0b\x42\x45\x46ORE_AUTH\x10\x01\x12\x10\n\x0cWITHOUT_AUTH\x10\x02*0\n\x11TemperatureFormat\x12\x0e\n\nFAHRENHEIT\x10\x00\x12\x0b\n\x07\x43\x45LSIUS\x10\x01*F\n\x12MaskDetectionLevel\x12\x0b\n\x07NOT_USE\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\r\n\tVERY_HIGH\x10\x03\x32\xc0\x02\n\x07Thermal\x12\x42\n\tGetConfig\x12\x19.thermal.GetConfigRequest\x1a\x1a.thermal.GetConfigResponse\x12\x42\n\tSetConfig\x12\x19.thermal.SetConfigRequest\x1a\x1a.thermal.SetConfigResponse\x12Q\n\x0eSetConfigMulti\x12\x1e.thermal.SetConfigMultiRequest\x1a\x1f.thermal.SetConfigMultiResponse\x12Z\n\x11GetTemperatureLog\x12!.thermal.GetTemperatureLogRequest\x1a\".thermal.GetTemperatureLogResponseB7\n\x1a\x63om.supremainc.sdk.thermalP\x01Z\x17\x62iostar/service/thermalb\x06proto3')
  ,
  dependencies=[err__pb2.DESCRIPTOR,])

_CHECKMODE = _descriptor.EnumDescriptor(
  name='CheckMode',
  full_name='thermal.CheckMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HARD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1331,
  serialized_end=1371,
)
_sym_db.RegisterEnumDescriptor(_CHECKMODE)

CheckMode = enum_type_wrapper.EnumTypeWrapper(_CHECKMODE)
_CHECKORDER = _descriptor.EnumDescriptor(
  name='CheckOrder',
  full_name='thermal.CheckOrder',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AFTER_AUTH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEFORE_AUTH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WITHOUT_AUTH', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1373,
  serialized_end=1436,
)
_sym_db.RegisterEnumDescriptor(_CHECKORDER)

CheckOrder = enum_type_wrapper.EnumTypeWrapper(_CHECKORDER)
_TEMPERATUREFORMAT = _descriptor.EnumDescriptor(
  name='TemperatureFormat',
  full_name='thermal.TemperatureFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAHRENHEIT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CELSIUS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1438,
  serialized_end=1486,
)
_sym_db.RegisterEnumDescriptor(_TEMPERATUREFORMAT)

TemperatureFormat = enum_type_wrapper.EnumTypeWrapper(_TEMPERATUREFORMAT)
_MASKDETECTIONLEVEL = _descriptor.EnumDescriptor(
  name='MaskDetectionLevel',
  full_name='thermal.MaskDetectionLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_USE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERY_HIGH', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1488,
  serialized_end=1558,
)
_sym_db.RegisterEnumDescriptor(_MASKDETECTIONLEVEL)

MaskDetectionLevel = enum_type_wrapper.EnumTypeWrapper(_MASKDETECTIONLEVEL)
OFF = 0
HARD = 1
SOFT = 2
AFTER_AUTH = 0
BEFORE_AUTH = 1
WITHOUT_AUTH = 2
FAHRENHEIT = 0
CELSIUS = 1
NOT_USE = 0
NORMAL = 1
HIGH = 2
VERY_HIGH = 3



_THERMALCAMERAROI = _descriptor.Descriptor(
  name='ThermalCameraROI',
  full_name='thermal.ThermalCameraROI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='thermal.ThermalCameraROI.x', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='thermal.ThermalCameraROI.y', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='thermal.ThermalCameraROI.width', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='thermal.ThermalCameraROI.height', index=3,
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
  serialized_start=37,
  serialized_end=108,
)


_THERMALCAMERA = _descriptor.Descriptor(
  name='ThermalCamera',
  full_name='thermal.ThermalCamera',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='distance', full_name='thermal.ThermalCamera.distance', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emissionRate', full_name='thermal.ThermalCamera.emissionRate', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ROI', full_name='thermal.ThermalCamera.ROI', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='useBodyCompensation', full_name='thermal.ThermalCamera.useBodyCompensation', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compensationTemperature', full_name='thermal.ThermalCamera.compensationTemperature', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=111,
  serialized_end=268,
)


_THERMALCONFIG = _descriptor.Descriptor(
  name='ThermalConfig',
  full_name='thermal.ThermalConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='checkMode', full_name='thermal.ThermalConfig.checkMode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkOrder', full_name='thermal.ThermalConfig.checkOrder', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperatureFormat', full_name='thermal.ThermalConfig.temperatureFormat', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperatureThreshold', full_name='thermal.ThermalConfig.temperatureThreshold', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auditTemperature', full_name='thermal.ThermalConfig.auditTemperature', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='useRejectSound', full_name='thermal.ThermalConfig.useRejectSound', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='useOverlapThermal', full_name='thermal.ThermalConfig.useOverlapThermal', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='camera', full_name='thermal.ThermalConfig.camera', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maskCheckMode', full_name='thermal.ThermalConfig.maskCheckMode', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maskDetectionLevel', full_name='thermal.ThermalConfig.maskDetectionLevel', index=9,
      number=10, type=14, cpp_type=8, label=1,
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
  serialized_start=271,
  serialized_end=668,
)


_GETCONFIGREQUEST = _descriptor.Descriptor(
  name='GetConfigRequest',
  full_name='thermal.GetConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='thermal.GetConfigRequest.deviceID', index=0,
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
  serialized_start=670,
  serialized_end=706,
)


_GETCONFIGRESPONSE = _descriptor.Descriptor(
  name='GetConfigResponse',
  full_name='thermal.GetConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='thermal.GetConfigResponse.config', index=0,
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
  serialized_start=708,
  serialized_end=767,
)


_SETCONFIGREQUEST = _descriptor.Descriptor(
  name='SetConfigRequest',
  full_name='thermal.SetConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='thermal.SetConfigRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='thermal.SetConfigRequest.config', index=1,
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
  serialized_start=769,
  serialized_end=845,
)


_SETCONFIGRESPONSE = _descriptor.Descriptor(
  name='SetConfigResponse',
  full_name='thermal.SetConfigResponse',
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
  serialized_start=847,
  serialized_end=866,
)


_SETCONFIGMULTIREQUEST = _descriptor.Descriptor(
  name='SetConfigMultiRequest',
  full_name='thermal.SetConfigMultiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceIDs', full_name='thermal.SetConfigMultiRequest.deviceIDs', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='config', full_name='thermal.SetConfigMultiRequest.config', index=1,
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
  serialized_start=868,
  serialized_end=950,
)


_SETCONFIGMULTIRESPONSE = _descriptor.Descriptor(
  name='SetConfigMultiResponse',
  full_name='thermal.SetConfigMultiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceErrors', full_name='thermal.SetConfigMultiResponse.deviceErrors', index=0,
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
  serialized_start=952,
  serialized_end=1018,
)


_TEMPERATURELOG = _descriptor.Descriptor(
  name='TemperatureLog',
  full_name='thermal.TemperatureLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='thermal.TemperatureLog.ID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='thermal.TemperatureLog.timestamp', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='thermal.TemperatureLog.deviceID', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userID', full_name='thermal.TemperatureLog.userID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventCode', full_name='thermal.TemperatureLog.eventCode', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subCode', full_name='thermal.TemperatureLog.subCode', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='thermal.TemperatureLog.temperature', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=1021,
  serialized_end=1159,
)


_GETTEMPERATURELOGREQUEST = _descriptor.Descriptor(
  name='GetTemperatureLogRequest',
  full_name='thermal.GetTemperatureLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='thermal.GetTemperatureLogRequest.deviceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startEventID', full_name='thermal.GetTemperatureLogRequest.startEventID', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxNumOfLog', full_name='thermal.GetTemperatureLogRequest.maxNumOfLog', index=2,
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
  serialized_start=1161,
  serialized_end=1248,
)


_GETTEMPERATURELOGRESPONSE = _descriptor.Descriptor(
  name='GetTemperatureLogResponse',
  full_name='thermal.GetTemperatureLogResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='temperatureEvents', full_name='thermal.GetTemperatureLogResponse.temperatureEvents', index=0,
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
  serialized_start=1250,
  serialized_end=1329,
)

_THERMALCAMERA.fields_by_name['ROI'].message_type = _THERMALCAMERAROI
_THERMALCONFIG.fields_by_name['checkMode'].enum_type = _CHECKMODE
_THERMALCONFIG.fields_by_name['checkOrder'].enum_type = _CHECKORDER
_THERMALCONFIG.fields_by_name['temperatureFormat'].enum_type = _TEMPERATUREFORMAT
_THERMALCONFIG.fields_by_name['camera'].message_type = _THERMALCAMERA
_THERMALCONFIG.fields_by_name['maskCheckMode'].enum_type = _CHECKMODE
_THERMALCONFIG.fields_by_name['maskDetectionLevel'].enum_type = _MASKDETECTIONLEVEL
_GETCONFIGRESPONSE.fields_by_name['config'].message_type = _THERMALCONFIG
_SETCONFIGREQUEST.fields_by_name['config'].message_type = _THERMALCONFIG
_SETCONFIGMULTIREQUEST.fields_by_name['config'].message_type = _THERMALCONFIG
_SETCONFIGMULTIRESPONSE.fields_by_name['deviceErrors'].message_type = err__pb2._ERRORRESPONSE
_GETTEMPERATURELOGRESPONSE.fields_by_name['temperatureEvents'].message_type = _TEMPERATURELOG
DESCRIPTOR.message_types_by_name['ThermalCameraROI'] = _THERMALCAMERAROI
DESCRIPTOR.message_types_by_name['ThermalCamera'] = _THERMALCAMERA
DESCRIPTOR.message_types_by_name['ThermalConfig'] = _THERMALCONFIG
DESCRIPTOR.message_types_by_name['GetConfigRequest'] = _GETCONFIGREQUEST
DESCRIPTOR.message_types_by_name['GetConfigResponse'] = _GETCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['SetConfigRequest'] = _SETCONFIGREQUEST
DESCRIPTOR.message_types_by_name['SetConfigResponse'] = _SETCONFIGRESPONSE
DESCRIPTOR.message_types_by_name['SetConfigMultiRequest'] = _SETCONFIGMULTIREQUEST
DESCRIPTOR.message_types_by_name['SetConfigMultiResponse'] = _SETCONFIGMULTIRESPONSE
DESCRIPTOR.message_types_by_name['TemperatureLog'] = _TEMPERATURELOG
DESCRIPTOR.message_types_by_name['GetTemperatureLogRequest'] = _GETTEMPERATURELOGREQUEST
DESCRIPTOR.message_types_by_name['GetTemperatureLogResponse'] = _GETTEMPERATURELOGRESPONSE
DESCRIPTOR.enum_types_by_name['CheckMode'] = _CHECKMODE
DESCRIPTOR.enum_types_by_name['CheckOrder'] = _CHECKORDER
DESCRIPTOR.enum_types_by_name['TemperatureFormat'] = _TEMPERATUREFORMAT
DESCRIPTOR.enum_types_by_name['MaskDetectionLevel'] = _MASKDETECTIONLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThermalCameraROI = _reflection.GeneratedProtocolMessageType('ThermalCameraROI', (_message.Message,), dict(
  DESCRIPTOR = _THERMALCAMERAROI,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.ThermalCameraROI)
  ))
_sym_db.RegisterMessage(ThermalCameraROI)

ThermalCamera = _reflection.GeneratedProtocolMessageType('ThermalCamera', (_message.Message,), dict(
  DESCRIPTOR = _THERMALCAMERA,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.ThermalCamera)
  ))
_sym_db.RegisterMessage(ThermalCamera)

ThermalConfig = _reflection.GeneratedProtocolMessageType('ThermalConfig', (_message.Message,), dict(
  DESCRIPTOR = _THERMALCONFIG,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.ThermalConfig)
  ))
_sym_db.RegisterMessage(ThermalConfig)

GetConfigRequest = _reflection.GeneratedProtocolMessageType('GetConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGREQUEST,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.GetConfigRequest)
  ))
_sym_db.RegisterMessage(GetConfigRequest)

GetConfigResponse = _reflection.GeneratedProtocolMessageType('GetConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCONFIGRESPONSE,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.GetConfigResponse)
  ))
_sym_db.RegisterMessage(GetConfigResponse)

SetConfigRequest = _reflection.GeneratedProtocolMessageType('SetConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGREQUEST,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.SetConfigRequest)
  ))
_sym_db.RegisterMessage(SetConfigRequest)

SetConfigResponse = _reflection.GeneratedProtocolMessageType('SetConfigResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGRESPONSE,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.SetConfigResponse)
  ))
_sym_db.RegisterMessage(SetConfigResponse)

SetConfigMultiRequest = _reflection.GeneratedProtocolMessageType('SetConfigMultiRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGMULTIREQUEST,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.SetConfigMultiRequest)
  ))
_sym_db.RegisterMessage(SetConfigMultiRequest)

SetConfigMultiResponse = _reflection.GeneratedProtocolMessageType('SetConfigMultiResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETCONFIGMULTIRESPONSE,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.SetConfigMultiResponse)
  ))
_sym_db.RegisterMessage(SetConfigMultiResponse)

TemperatureLog = _reflection.GeneratedProtocolMessageType('TemperatureLog', (_message.Message,), dict(
  DESCRIPTOR = _TEMPERATURELOG,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.TemperatureLog)
  ))
_sym_db.RegisterMessage(TemperatureLog)

GetTemperatureLogRequest = _reflection.GeneratedProtocolMessageType('GetTemperatureLogRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTEMPERATURELOGREQUEST,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.GetTemperatureLogRequest)
  ))
_sym_db.RegisterMessage(GetTemperatureLogRequest)

GetTemperatureLogResponse = _reflection.GeneratedProtocolMessageType('GetTemperatureLogResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETTEMPERATURELOGRESPONSE,
  __module__ = 'thermal_pb2'
  # @@protoc_insertion_point(class_scope:thermal.GetTemperatureLogResponse)
  ))
_sym_db.RegisterMessage(GetTemperatureLogResponse)


DESCRIPTOR._options = None

_THERMAL = _descriptor.ServiceDescriptor(
  name='Thermal',
  full_name='thermal.Thermal',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1561,
  serialized_end=1881,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetConfig',
    full_name='thermal.Thermal.GetConfig',
    index=0,
    containing_service=None,
    input_type=_GETCONFIGREQUEST,
    output_type=_GETCONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetConfig',
    full_name='thermal.Thermal.SetConfig',
    index=1,
    containing_service=None,
    input_type=_SETCONFIGREQUEST,
    output_type=_SETCONFIGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetConfigMulti',
    full_name='thermal.Thermal.SetConfigMulti',
    index=2,
    containing_service=None,
    input_type=_SETCONFIGMULTIREQUEST,
    output_type=_SETCONFIGMULTIRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTemperatureLog',
    full_name='thermal.Thermal.GetTemperatureLog',
    index=3,
    containing_service=None,
    input_type=_GETTEMPERATURELOGREQUEST,
    output_type=_GETTEMPERATURELOGRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_THERMAL)

DESCRIPTOR.services_by_name['Thermal'] = _THERMAL

# @@protoc_insertion_point(module_scope)
