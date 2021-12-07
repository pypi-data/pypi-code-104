# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grid/v1/sshpublickey.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from grid.protos.grid.v1 import metadata_pb2 as grid_dot_v1_dot_metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='grid/v1/sshpublickey.proto',
  package='grid.v1',
  syntax='proto3',
  serialized_options=b'Z0github.com/gridai/grid/grid-backend/apis/grid/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1agrid/v1/sshpublickey.proto\x12\x07grid.v1\x1a\x16grid/v1/metadata.proto\"\xdf\x01\n\x0cSSHPublicKey\x12-\n\x08metadata\x18\x01 \x01(\x0b\x32\x11.grid.v1.MetadataR\x08metadata\x12\x1d\n\npublic_key\x18\x02 \x01(\tR\tpublicKey\x12\x19\n\x08key_type\x18\x03 \x01(\tR\x07keyType\x12\x18\n\x07\x63omment\x18\x04 \x01(\tR\x07\x63omment\x12\x17\n\x07user_id\x18\x05 \x01(\tR\x06userId\x12\x33\n\x06status\x18\x06 \x01(\x0b\x32\x1b.grid.v1.SSHPublicKeyStatusR\x06status\"\x14\n\x12SSHPublicKeyStatusB2Z0github.com/gridai/grid/grid-backend/apis/grid/v1b\x06proto3'
  ,
  dependencies=[grid_dot_v1_dot_metadata__pb2.DESCRIPTOR,])




_SSHPUBLICKEY = _descriptor.Descriptor(
  name='SSHPublicKey',
  full_name='grid.v1.SSHPublicKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='grid.v1.SSHPublicKey.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metadata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='grid.v1.SSHPublicKey.public_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='publicKey', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_type', full_name='grid.v1.SSHPublicKey.key_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keyType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment', full_name='grid.v1.SSHPublicKey.comment', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='comment', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='grid.v1.SSHPublicKey.user_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='grid.v1.SSHPublicKey.status', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=64,
  serialized_end=287,
)


_SSHPUBLICKEYSTATUS = _descriptor.Descriptor(
  name='SSHPublicKeyStatus',
  full_name='grid.v1.SSHPublicKeyStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=289,
  serialized_end=309,
)

_SSHPUBLICKEY.fields_by_name['metadata'].message_type = grid_dot_v1_dot_metadata__pb2._METADATA
_SSHPUBLICKEY.fields_by_name['status'].message_type = _SSHPUBLICKEYSTATUS
DESCRIPTOR.message_types_by_name['SSHPublicKey'] = _SSHPUBLICKEY
DESCRIPTOR.message_types_by_name['SSHPublicKeyStatus'] = _SSHPUBLICKEYSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SSHPublicKey = _reflection.GeneratedProtocolMessageType('SSHPublicKey', (_message.Message,), {
  'DESCRIPTOR' : _SSHPUBLICKEY,
  '__module__' : 'grid.v1.sshpublickey_pb2'
  # @@protoc_insertion_point(class_scope:grid.v1.SSHPublicKey)
  })
_sym_db.RegisterMessage(SSHPublicKey)

SSHPublicKeyStatus = _reflection.GeneratedProtocolMessageType('SSHPublicKeyStatus', (_message.Message,), {
  'DESCRIPTOR' : _SSHPUBLICKEYSTATUS,
  '__module__' : 'grid.v1.sshpublickey_pb2'
  # @@protoc_insertion_point(class_scope:grid.v1.SSHPublicKeyStatus)
  })
_sym_db.RegisterMessage(SSHPublicKeyStatus)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
