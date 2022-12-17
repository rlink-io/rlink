# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zone.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='zone.proto',
  package='zone',
  syntax='proto3',
  serialized_options=_b('\n\027com.supremainc.sdk.zoneP\001Z\024biostar/service/zone'),
  serialized_pb=_b('\n\nzone.proto\x12\x04zone\"L\n\nZoneStatus\x12\x0e\n\x06zoneID\x18\x01 \x01(\r\x12\x1c\n\x06status\x18\x02 \x01(\x0e\x32\x0c.zone.Status\x12\x10\n\x08\x64isabled\x18\x03 \x01(\x08*p\n\x04Type\x12\x07\n\x03\x41PB\x10\x00\x12\r\n\tTIMED_APB\x10\x01\x12\x0e\n\nFIRE_ALARM\x10\x02\x12\x12\n\x0eSCHEDULED_LOCK\x10\x03\x12\x13\n\x0fINTRUSION_ALARM\x10\x04\x12\r\n\tINTERLOCK\x10\x05\x12\x08\n\x04LIFT\x10\x06*|\n\x06Status\x12\n\n\x06NORMAL\x10\x00\x12\x0b\n\x07\x41LARMED\x10\x01\x12\n\n\x06LOCKED\x10\x02\x12\x0c\n\x08UNLOCKED\x10\x04\x12\x0f\n\x0bLIFT_LOCKED\x10\x02\x12\x11\n\rLIFT_UNLOCKED\x10\x04\x12\t\n\x05\x41RMED\x10\x08\x12\x0c\n\x08\x44ISARMED\x10\x00\x1a\x02\x10\x01\x42\x31\n\x17\x63om.supremainc.sdk.zoneP\x01Z\x14\x62iostar/service/zoneb\x06proto3')
)

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='zone.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='APB', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMED_APB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRE_ALARM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCHEDULED_LOCK', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTRUSION_ALARM', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERLOCK', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=98,
  serialized_end=210,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='zone.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALARMED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCKED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNLOCKED', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFT_LOCKED', index=4, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFT_UNLOCKED', index=5, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARMED', index=6, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISARMED', index=7, number=0,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=_b('\020\001'),
  serialized_start=212,
  serialized_end=336,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
APB = 0
TIMED_APB = 1
FIRE_ALARM = 2
SCHEDULED_LOCK = 3
INTRUSION_ALARM = 4
INTERLOCK = 5
LIFT = 6
NORMAL = 0
ALARMED = 1
LOCKED = 2
UNLOCKED = 4
LIFT_LOCKED = 2
LIFT_UNLOCKED = 4
ARMED = 8
DISARMED = 0



_ZONESTATUS = _descriptor.Descriptor(
  name='ZoneStatus',
  full_name='zone.ZoneStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zoneID', full_name='zone.ZoneStatus.zoneID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='zone.ZoneStatus.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='zone.ZoneStatus.disabled', index=2,
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
  serialized_start=20,
  serialized_end=96,
)

_ZONESTATUS.fields_by_name['status'].enum_type = _STATUS
DESCRIPTOR.message_types_by_name['ZoneStatus'] = _ZONESTATUS
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZoneStatus = _reflection.GeneratedProtocolMessageType('ZoneStatus', (_message.Message,), dict(
  DESCRIPTOR = _ZONESTATUS,
  __module__ = 'zone_pb2'
  # @@protoc_insertion_point(class_scope:zone.ZoneStatus)
  ))
_sym_db.RegisterMessage(ZoneStatus)


DESCRIPTOR._options = None
_STATUS._options = None
# @@protoc_insertion_point(module_scope)
