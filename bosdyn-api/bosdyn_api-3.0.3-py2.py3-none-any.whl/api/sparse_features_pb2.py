# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bosdyn/api/sparse_features.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bosdyn.api import geometry_pb2 as bosdyn_dot_api_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bosdyn/api/sparse_features.proto',
  package='bosdyn.api',
  syntax='proto3',
  serialized_pb=_b('\n bosdyn/api/sparse_features.proto\x12\nbosdyn.api\x1a\x19\x62osdyn/api/geometry.proto\"x\n\x08Keypoint\x12%\n\x0b\x63oordinates\x18\x02 \x01(\x0b\x32\x10.bosdyn.api.Vec2\x12\x19\n\x11\x62inary_descriptor\x18\x03 \x01(\x0c\x12\r\n\x05score\x18\x04 \x01(\x02\x12\x0c\n\x04size\x18\x05 \x01(\x02\x12\r\n\x05\x61ngle\x18\x06 \x01(\x02\"\xb7\x01\n\x0bKeypointSet\x12\'\n\tkeypoints\x18\x02 \x03(\x0b\x32\x14.bosdyn.api.Keypoint\x12\x32\n\x04type\x18\x03 \x01(\x0e\x32$.bosdyn.api.KeypointSet.KeypointType\"K\n\x0cKeypointType\x12\x14\n\x10KEYPOINT_UNKNOWN\x10\x00\x12\x13\n\x0fKEYPOINT_SIMPLE\x10\x01\x12\x10\n\x0cKEYPOINT_ORB\x10\x02\"F\n\x05Match\x12\x17\n\x0freference_index\x18\x02 \x01(\x05\x12\x12\n\nlive_index\x18\x03 \x01(\x05\x12\x10\n\x08\x64istance\x18\x04 \x01(\x02\"\x9c\x01\n\x0fKeypointMatches\x12\x34\n\x13reference_keypoints\x18\x02 \x01(\x0b\x32\x17.bosdyn.api.KeypointSet\x12/\n\x0elive_keypoints\x18\x03 \x01(\x0b\x32\x17.bosdyn.api.KeypointSet\x12\"\n\x07matches\x18\x04 \x03(\x0b\x32\x11.bosdyn.api.MatchB\x15\x42\x13SparseFeaturesProtob\x06proto3')
  ,
  dependencies=[bosdyn_dot_api_dot_geometry__pb2.DESCRIPTOR,])



_KEYPOINTSET_KEYPOINTTYPE = _descriptor.EnumDescriptor(
  name='KeypointType',
  full_name='bosdyn.api.KeypointSet.KeypointType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KEYPOINT_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYPOINT_SIMPLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYPOINT_ORB', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=306,
  serialized_end=381,
)
_sym_db.RegisterEnumDescriptor(_KEYPOINTSET_KEYPOINTTYPE)


_KEYPOINT = _descriptor.Descriptor(
  name='Keypoint',
  full_name='bosdyn.api.Keypoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coordinates', full_name='bosdyn.api.Keypoint.coordinates', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_descriptor', full_name='bosdyn.api.Keypoint.binary_descriptor', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='bosdyn.api.Keypoint.score', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='bosdyn.api.Keypoint.size', index=3,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle', full_name='bosdyn.api.Keypoint.angle', index=4,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=195,
)


_KEYPOINTSET = _descriptor.Descriptor(
  name='KeypointSet',
  full_name='bosdyn.api.KeypointSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keypoints', full_name='bosdyn.api.KeypointSet.keypoints', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='bosdyn.api.KeypointSet.type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KEYPOINTSET_KEYPOINTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=381,
)


_MATCH = _descriptor.Descriptor(
  name='Match',
  full_name='bosdyn.api.Match',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_index', full_name='bosdyn.api.Match.reference_index', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='live_index', full_name='bosdyn.api.Match.live_index', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='bosdyn.api.Match.distance', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=453,
)


_KEYPOINTMATCHES = _descriptor.Descriptor(
  name='KeypointMatches',
  full_name='bosdyn.api.KeypointMatches',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_keypoints', full_name='bosdyn.api.KeypointMatches.reference_keypoints', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='live_keypoints', full_name='bosdyn.api.KeypointMatches.live_keypoints', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matches', full_name='bosdyn.api.KeypointMatches.matches', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=612,
)

_KEYPOINT.fields_by_name['coordinates'].message_type = bosdyn_dot_api_dot_geometry__pb2._VEC2
_KEYPOINTSET.fields_by_name['keypoints'].message_type = _KEYPOINT
_KEYPOINTSET.fields_by_name['type'].enum_type = _KEYPOINTSET_KEYPOINTTYPE
_KEYPOINTSET_KEYPOINTTYPE.containing_type = _KEYPOINTSET
_KEYPOINTMATCHES.fields_by_name['reference_keypoints'].message_type = _KEYPOINTSET
_KEYPOINTMATCHES.fields_by_name['live_keypoints'].message_type = _KEYPOINTSET
_KEYPOINTMATCHES.fields_by_name['matches'].message_type = _MATCH
DESCRIPTOR.message_types_by_name['Keypoint'] = _KEYPOINT
DESCRIPTOR.message_types_by_name['KeypointSet'] = _KEYPOINTSET
DESCRIPTOR.message_types_by_name['Match'] = _MATCH
DESCRIPTOR.message_types_by_name['KeypointMatches'] = _KEYPOINTMATCHES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Keypoint = _reflection.GeneratedProtocolMessageType('Keypoint', (_message.Message,), dict(
  DESCRIPTOR = _KEYPOINT,
  __module__ = 'bosdyn.api.sparse_features_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.Keypoint)
  ))
_sym_db.RegisterMessage(Keypoint)

KeypointSet = _reflection.GeneratedProtocolMessageType('KeypointSet', (_message.Message,), dict(
  DESCRIPTOR = _KEYPOINTSET,
  __module__ = 'bosdyn.api.sparse_features_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.KeypointSet)
  ))
_sym_db.RegisterMessage(KeypointSet)

Match = _reflection.GeneratedProtocolMessageType('Match', (_message.Message,), dict(
  DESCRIPTOR = _MATCH,
  __module__ = 'bosdyn.api.sparse_features_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.Match)
  ))
_sym_db.RegisterMessage(Match)

KeypointMatches = _reflection.GeneratedProtocolMessageType('KeypointMatches', (_message.Message,), dict(
  DESCRIPTOR = _KEYPOINTMATCHES,
  __module__ = 'bosdyn.api.sparse_features_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.KeypointMatches)
  ))
_sym_db.RegisterMessage(KeypointMatches)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\023SparseFeaturesProto'))
# @@protoc_insertion_point(module_scope)
