# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily_analytics/v1/daily_volatility.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='systemathics/apis/services/daily_analytics/v1/daily_volatility.proto',
  package='systemathics.apis.services.daily_analytics.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDsystemathics/apis/services/daily_analytics/v1/daily_volatility.proto\x12-systemathics.apis.services.daily_analytics.v1\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\"\xb2\x01\n\x16\x44\x61ilyVolatilityRequest\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\x12\x12\n\nadjustment\x18\x03 \x01(\x08\"(\n\x17\x44\x61ilyVolatilityResponse\x12\r\n\x05value\x18\x01 \x01(\x01\x32\xbb\x01\n\x16\x44\x61ilyVolatilityService\x12\xa0\x01\n\x0f\x44\x61ilyVolatility\x12\x45.systemathics.apis.services.daily_analytics.v1.DailyVolatilityRequest\x1a\x46.systemathics.apis.services.daily_analytics.v1.DailyVolatilityResponseb\x06proto3'
  ,
  dependencies=[systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2.DESCRIPTOR,])




_DAILYVOLATILITYREQUEST = _descriptor.Descriptor(
  name='DailyVolatilityRequest',
  full_name='systemathics.apis.services.daily_analytics.v1.DailyVolatilityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='systemathics.apis.services.daily_analytics.v1.DailyVolatilityRequest.identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='systemathics.apis.services.daily_analytics.v1.DailyVolatilityRequest.constraints', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjustment', full_name='systemathics.apis.services.daily_analytics.v1.DailyVolatilityRequest.adjustment', index=2,
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
  serialized_start=223,
  serialized_end=401,
)


_DAILYVOLATILITYRESPONSE = _descriptor.Descriptor(
  name='DailyVolatilityResponse',
  full_name='systemathics.apis.services.daily_analytics.v1.DailyVolatilityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='systemathics.apis.services.daily_analytics.v1.DailyVolatilityResponse.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=403,
  serialized_end=443,
)

_DAILYVOLATILITYREQUEST.fields_by_name['identifier'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2._IDENTIFIER
_DAILYVOLATILITYREQUEST.fields_by_name['constraints'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2._CONSTRAINTS
DESCRIPTOR.message_types_by_name['DailyVolatilityRequest'] = _DAILYVOLATILITYREQUEST
DESCRIPTOR.message_types_by_name['DailyVolatilityResponse'] = _DAILYVOLATILITYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyVolatilityRequest = _reflection.GeneratedProtocolMessageType('DailyVolatilityRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYVOLATILITYREQUEST,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_volatility_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyVolatilityRequest)
  })
_sym_db.RegisterMessage(DailyVolatilityRequest)

DailyVolatilityResponse = _reflection.GeneratedProtocolMessageType('DailyVolatilityResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYVOLATILITYRESPONSE,
  '__module__' : 'systemathics.apis.services.daily_analytics.v1.daily_volatility_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily_analytics.v1.DailyVolatilityResponse)
  })
_sym_db.RegisterMessage(DailyVolatilityResponse)



_DAILYVOLATILITYSERVICE = _descriptor.ServiceDescriptor(
  name='DailyVolatilityService',
  full_name='systemathics.apis.services.daily_analytics.v1.DailyVolatilityService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=446,
  serialized_end=633,
  methods=[
  _descriptor.MethodDescriptor(
    name='DailyVolatility',
    full_name='systemathics.apis.services.daily_analytics.v1.DailyVolatilityService.DailyVolatility',
    index=0,
    containing_service=None,
    input_type=_DAILYVOLATILITYREQUEST,
    output_type=_DAILYVOLATILITYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAILYVOLATILITYSERVICE)

DESCRIPTOR.services_by_name['DailyVolatilityService'] = _DAILYVOLATILITYSERVICE

# @@protoc_insertion_point(module_scope)
