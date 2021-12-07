# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v1/daily_bars.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='systemathics/apis/services/daily/v1/daily_bars.proto',
  package='systemathics.apis.services.daily.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4systemathics/apis/services/daily/v1/daily_bars.proto\x12#systemathics.apis.services.daily.v1\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\"\xac\x01\n\x10\x44\x61ilyBarsRequest\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\x12\x12\n\nadjustment\x18\x03 \x01(\x08\"P\n\x11\x44\x61ilyBarsResponse\x12;\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32-.systemathics.apis.services.daily.v1.DailyBar\"s\n\x08\x44\x61ilyBar\x12\x1f\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.Date\x12\x0c\n\x04open\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0b\n\x03low\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0e\n\x06volume\x18\x06 \x01(\x03\x32\x8e\x01\n\x10\x44\x61ilyBarsService\x12z\n\tDailyBars\x12\x35.systemathics.apis.services.daily.v1.DailyBarsRequest\x1a\x36.systemathics.apis.services.daily.v1.DailyBarsResponseb\x06proto3'
  ,
  dependencies=[google_dot_type_dot_date__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2.DESCRIPTOR,])




_DAILYBARSREQUEST = _descriptor.Descriptor(
  name='DailyBarsRequest',
  full_name='systemathics.apis.services.daily.v1.DailyBarsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='systemathics.apis.services.daily.v1.DailyBarsRequest.identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='systemathics.apis.services.daily.v1.DailyBarsRequest.constraints', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjustment', full_name='systemathics.apis.services.daily.v1.DailyBarsRequest.adjustment', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=221,
  serialized_end=393,
)


_DAILYBARSRESPONSE = _descriptor.Descriptor(
  name='DailyBarsResponse',
  full_name='systemathics.apis.services.daily.v1.DailyBarsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='systemathics.apis.services.daily.v1.DailyBarsResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=395,
  serialized_end=475,
)


_DAILYBAR = _descriptor.Descriptor(
  name='DailyBar',
  full_name='systemathics.apis.services.daily.v1.DailyBar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='systemathics.apis.services.daily.v1.DailyBar.date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='open', full_name='systemathics.apis.services.daily.v1.DailyBar.open', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high', full_name='systemathics.apis.services.daily.v1.DailyBar.high', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low', full_name='systemathics.apis.services.daily.v1.DailyBar.low', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='close', full_name='systemathics.apis.services.daily.v1.DailyBar.close', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='systemathics.apis.services.daily.v1.DailyBar.volume', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=477,
  serialized_end=592,
)

_DAILYBARSREQUEST.fields_by_name['identifier'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2._IDENTIFIER
_DAILYBARSREQUEST.fields_by_name['constraints'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2._CONSTRAINTS
_DAILYBARSRESPONSE.fields_by_name['data'].message_type = _DAILYBAR
_DAILYBAR.fields_by_name['date'].message_type = google_dot_type_dot_date__pb2._DATE
DESCRIPTOR.message_types_by_name['DailyBarsRequest'] = _DAILYBARSREQUEST
DESCRIPTOR.message_types_by_name['DailyBarsResponse'] = _DAILYBARSRESPONSE
DESCRIPTOR.message_types_by_name['DailyBar'] = _DAILYBAR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyBarsRequest = _reflection.GeneratedProtocolMessageType('DailyBarsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBARSREQUEST,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_bars_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyBarsRequest)
  })
_sym_db.RegisterMessage(DailyBarsRequest)

DailyBarsResponse = _reflection.GeneratedProtocolMessageType('DailyBarsResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBARSRESPONSE,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_bars_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyBarsResponse)
  })
_sym_db.RegisterMessage(DailyBarsResponse)

DailyBar = _reflection.GeneratedProtocolMessageType('DailyBar', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBAR,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_bars_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyBar)
  })
_sym_db.RegisterMessage(DailyBar)



_DAILYBARSSERVICE = _descriptor.ServiceDescriptor(
  name='DailyBarsService',
  full_name='systemathics.apis.services.daily.v1.DailyBarsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=595,
  serialized_end=737,
  methods=[
  _descriptor.MethodDescriptor(
    name='DailyBars',
    full_name='systemathics.apis.services.daily.v1.DailyBarsService.DailyBars',
    index=0,
    containing_service=None,
    input_type=_DAILYBARSREQUEST,
    output_type=_DAILYBARSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAILYBARSSERVICE)

DESCRIPTOR.services_by_name['DailyBarsService'] = _DAILYBARSSERVICE

# @@protoc_insertion_point(module_scope)
