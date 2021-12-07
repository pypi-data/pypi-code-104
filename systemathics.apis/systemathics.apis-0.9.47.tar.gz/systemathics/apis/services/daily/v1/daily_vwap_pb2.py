# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v1/daily_vwap.proto
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
  name='systemathics/apis/services/daily/v1/daily_vwap.proto',
  package='systemathics.apis.services.daily.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4systemathics/apis/services/daily/v1/daily_vwap.proto\x12#systemathics.apis.services.daily.v1\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\"\xad\x01\n\x11\x44\x61ilyVwapsRequest\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\x12\x12\n\nadjustment\x18\x03 \x01(\x08\"R\n\x12\x44\x61ilyVwapsResponse\x12<\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32..systemathics.apis.services.daily.v1.DailyVwap\"K\n\tDailyVwap\x12\x1f\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.Date\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0e\n\x06volume\x18\x03 \x01(\x03\x32\x92\x01\n\x11\x44\x61ilyVwapsService\x12}\n\nDailyVwaps\x12\x36.systemathics.apis.services.daily.v1.DailyVwapsRequest\x1a\x37.systemathics.apis.services.daily.v1.DailyVwapsResponseb\x06proto3'
  ,
  dependencies=[google_dot_type_dot_date__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2.DESCRIPTOR,systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2.DESCRIPTOR,])




_DAILYVWAPSREQUEST = _descriptor.Descriptor(
  name='DailyVwapsRequest',
  full_name='systemathics.apis.services.daily.v1.DailyVwapsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='identifier', full_name='systemathics.apis.services.daily.v1.DailyVwapsRequest.identifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='systemathics.apis.services.daily.v1.DailyVwapsRequest.constraints', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='adjustment', full_name='systemathics.apis.services.daily.v1.DailyVwapsRequest.adjustment', index=2,
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
  serialized_end=394,
)


_DAILYVWAPSRESPONSE = _descriptor.Descriptor(
  name='DailyVwapsResponse',
  full_name='systemathics.apis.services.daily.v1.DailyVwapsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='systemathics.apis.services.daily.v1.DailyVwapsResponse.data', index=0,
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
  serialized_start=396,
  serialized_end=478,
)


_DAILYVWAP = _descriptor.Descriptor(
  name='DailyVwap',
  full_name='systemathics.apis.services.daily.v1.DailyVwap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='systemathics.apis.services.daily.v1.DailyVwap.date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='systemathics.apis.services.daily.v1.DailyVwap.price', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume', full_name='systemathics.apis.services.daily.v1.DailyVwap.volume', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=480,
  serialized_end=555,
)

_DAILYVWAPSREQUEST.fields_by_name['identifier'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2._IDENTIFIER
_DAILYVWAPSREQUEST.fields_by_name['constraints'].message_type = systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2._CONSTRAINTS
_DAILYVWAPSRESPONSE.fields_by_name['data'].message_type = _DAILYVWAP
_DAILYVWAP.fields_by_name['date'].message_type = google_dot_type_dot_date__pb2._DATE
DESCRIPTOR.message_types_by_name['DailyVwapsRequest'] = _DAILYVWAPSREQUEST
DESCRIPTOR.message_types_by_name['DailyVwapsResponse'] = _DAILYVWAPSRESPONSE
DESCRIPTOR.message_types_by_name['DailyVwap'] = _DAILYVWAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DailyVwapsRequest = _reflection.GeneratedProtocolMessageType('DailyVwapsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYVWAPSREQUEST,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_vwap_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyVwapsRequest)
  })
_sym_db.RegisterMessage(DailyVwapsRequest)

DailyVwapsResponse = _reflection.GeneratedProtocolMessageType('DailyVwapsResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYVWAPSRESPONSE,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_vwap_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyVwapsResponse)
  })
_sym_db.RegisterMessage(DailyVwapsResponse)

DailyVwap = _reflection.GeneratedProtocolMessageType('DailyVwap', (_message.Message,), {
  'DESCRIPTOR' : _DAILYVWAP,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_vwap_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyVwap)
  })
_sym_db.RegisterMessage(DailyVwap)



_DAILYVWAPSSERVICE = _descriptor.ServiceDescriptor(
  name='DailyVwapsService',
  full_name='systemathics.apis.services.daily.v1.DailyVwapsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=558,
  serialized_end=704,
  methods=[
  _descriptor.MethodDescriptor(
    name='DailyVwaps',
    full_name='systemathics.apis.services.daily.v1.DailyVwapsService.DailyVwaps',
    index=0,
    containing_service=None,
    input_type=_DAILYVWAPSREQUEST,
    output_type=_DAILYVWAPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAILYVWAPSSERVICE)

DESCRIPTOR.services_by_name['DailyVwapsService'] = _DAILYVWAPSSERVICE

# @@protoc_insertion_point(module_scope)
