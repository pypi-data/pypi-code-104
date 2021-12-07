# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apps/Protos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='apps/Protos.proto',
  package='com.mammut.communication.transducers',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x61pps/Protos.proto\x12$com.mammut.communication.transducers\"\xcb\x01\n\x0f\x43oncreteThought\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07user_id\x18\x02 \x01(\x04\x12\x11\n\tuser_type\x18\x03 \x01(\t\x12\x13\n\x0buser_gender\x18\x04 \x01(\t\x12\x16\n\x0euser_birthdate\x18\x05 \x01(\t\x12\x12\n\nmachine_id\x18\x06 \x01(\x04\x12\x0f\n\x07room_id\x18\x07 \x01(\x04\x12\x11\n\troom_type\x18\x08 \x01(\t\x12\x0c\n\x04text\x18\t \x01(\x0c\x12\x15\n\rcreation_date\x18\n \x01(\t\"\x91\x06\n\x05Issue\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x13\n\x0b\x63ustom_code\x18\x02 \x01(\t\x12\x1b\n\x13\x63\x61usative_vertex_id\x18\x03 \x01(\x04\x12\x12\n\nmachine_id\x18\x04 \x01(\x04\x12\x0f\n\x07room_id\x18\x05 \x01(\x04\x12\x12\n\nissue_type\x18\x06 \x01(\t\x12\x13\n\x0bissue_state\x18\x07 \x01(\t\x12\x17\n\x0fresolution_text\x18\x08 \x01(\x0c\x12\x15\n\rcreation_date\x18\t \x01(\t\x12\x17\n\x0fresolution_date\x18\n \x01(\t\x12[\n\x12\x63onversation_scope\x18\x0b \x01(\x0b\x32?.com.mammut.communication.transducers.Issue.ConversationClosure\x12\x19\n\x11triggers_messages\x18\x0c \x03(\t\x1a\xba\x03\n\x13\x43onversationClosure\x12o\n\rsnapshotStack\x18\x01 \x03(\x0b\x32X.com.mammut.communication.transducers.Issue.ConversationClosure.GraphTransverseValuePair\x12z\n\x18snapshotKnownValuesStack\x18\x02 \x03(\x0b\x32X.com.mammut.communication.transducers.Issue.ConversationClosure.GraphTransverseValuePair\x12|\n\x1asnapshotUnknownValuesStack\x18\x03 \x03(\x0b\x32X.com.mammut.communication.transducers.Issue.ConversationClosure.GraphTransverseValuePair\x1a\x38\n\x18GraphTransverseValuePair\x12\r\n\x05steps\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB\x08\x42\x06Protosb\x06proto3')
)




_CONCRETETHOUGHT = _descriptor.Descriptor(
  name='ConcreteThought',
  full_name='com.mammut.communication.transducers.ConcreteThought',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.mammut.communication.transducers.ConcreteThought.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='com.mammut.communication.transducers.ConcreteThought.user_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='com.mammut.communication.transducers.ConcreteThought.user_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_gender', full_name='com.mammut.communication.transducers.ConcreteThought.user_gender', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_birthdate', full_name='com.mammut.communication.transducers.ConcreteThought.user_birthdate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='machine_id', full_name='com.mammut.communication.transducers.ConcreteThought.machine_id', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='com.mammut.communication.transducers.ConcreteThought.room_id', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_type', full_name='com.mammut.communication.transducers.ConcreteThought.room_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='com.mammut.communication.transducers.ConcreteThought.text', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='com.mammut.communication.transducers.ConcreteThought.creation_date', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=60,
  serialized_end=263,
)


_ISSUE_CONVERSATIONCLOSURE_GRAPHTRANSVERSEVALUEPAIR = _descriptor.Descriptor(
  name='GraphTransverseValuePair',
  full_name='com.mammut.communication.transducers.Issue.ConversationClosure.GraphTransverseValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steps', full_name='com.mammut.communication.transducers.Issue.ConversationClosure.GraphTransverseValuePair.steps', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.mammut.communication.transducers.Issue.ConversationClosure.GraphTransverseValuePair.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=995,
  serialized_end=1051,
)

_ISSUE_CONVERSATIONCLOSURE = _descriptor.Descriptor(
  name='ConversationClosure',
  full_name='com.mammut.communication.transducers.Issue.ConversationClosure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='snapshotStack', full_name='com.mammut.communication.transducers.Issue.ConversationClosure.snapshotStack', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshotKnownValuesStack', full_name='com.mammut.communication.transducers.Issue.ConversationClosure.snapshotKnownValuesStack', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='snapshotUnknownValuesStack', full_name='com.mammut.communication.transducers.Issue.ConversationClosure.snapshotUnknownValuesStack', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ISSUE_CONVERSATIONCLOSURE_GRAPHTRANSVERSEVALUEPAIR, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=1051,
)

_ISSUE = _descriptor.Descriptor(
  name='Issue',
  full_name='com.mammut.communication.transducers.Issue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='com.mammut.communication.transducers.Issue.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_code', full_name='com.mammut.communication.transducers.Issue.custom_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='causative_vertex_id', full_name='com.mammut.communication.transducers.Issue.causative_vertex_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='machine_id', full_name='com.mammut.communication.transducers.Issue.machine_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='com.mammut.communication.transducers.Issue.room_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issue_type', full_name='com.mammut.communication.transducers.Issue.issue_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issue_state', full_name='com.mammut.communication.transducers.Issue.issue_state', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution_text', full_name='com.mammut.communication.transducers.Issue.resolution_text', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='com.mammut.communication.transducers.Issue.creation_date', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution_date', full_name='com.mammut.communication.transducers.Issue.resolution_date', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversation_scope', full_name='com.mammut.communication.transducers.Issue.conversation_scope', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggers_messages', full_name='com.mammut.communication.transducers.Issue.triggers_messages', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ISSUE_CONVERSATIONCLOSURE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=266,
  serialized_end=1051,
)

_ISSUE_CONVERSATIONCLOSURE_GRAPHTRANSVERSEVALUEPAIR.containing_type = _ISSUE_CONVERSATIONCLOSURE
_ISSUE_CONVERSATIONCLOSURE.fields_by_name['snapshotStack'].message_type = _ISSUE_CONVERSATIONCLOSURE_GRAPHTRANSVERSEVALUEPAIR
_ISSUE_CONVERSATIONCLOSURE.fields_by_name['snapshotKnownValuesStack'].message_type = _ISSUE_CONVERSATIONCLOSURE_GRAPHTRANSVERSEVALUEPAIR
_ISSUE_CONVERSATIONCLOSURE.fields_by_name['snapshotUnknownValuesStack'].message_type = _ISSUE_CONVERSATIONCLOSURE_GRAPHTRANSVERSEVALUEPAIR
_ISSUE_CONVERSATIONCLOSURE.containing_type = _ISSUE
_ISSUE.fields_by_name['conversation_scope'].message_type = _ISSUE_CONVERSATIONCLOSURE
DESCRIPTOR.message_types_by_name['ConcreteThought'] = _CONCRETETHOUGHT
DESCRIPTOR.message_types_by_name['Issue'] = _ISSUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConcreteThought = _reflection.GeneratedProtocolMessageType('ConcreteThought', (_message.Message,), dict(
  DESCRIPTOR = _CONCRETETHOUGHT,
  __module__ = 'apps.Protos_pb2'
  # @@protoc_insertion_point(class_scope:com.mammut.communication.transducers.ConcreteThought)
  ))
_sym_db.RegisterMessage(ConcreteThought)

Issue = _reflection.GeneratedProtocolMessageType('Issue', (_message.Message,), dict(

  ConversationClosure = _reflection.GeneratedProtocolMessageType('ConversationClosure', (_message.Message,), dict(

    GraphTransverseValuePair = _reflection.GeneratedProtocolMessageType('GraphTransverseValuePair', (_message.Message,), dict(
      DESCRIPTOR = _ISSUE_CONVERSATIONCLOSURE_GRAPHTRANSVERSEVALUEPAIR,
      __module__ = 'apps.Protos_pb2'
      # @@protoc_insertion_point(class_scope:com.mammut.communication.transducers.Issue.ConversationClosure.GraphTransverseValuePair)
      ))
    ,
    DESCRIPTOR = _ISSUE_CONVERSATIONCLOSURE,
    __module__ = 'apps.Protos_pb2'
    # @@protoc_insertion_point(class_scope:com.mammut.communication.transducers.Issue.ConversationClosure)
    ))
  ,
  DESCRIPTOR = _ISSUE,
  __module__ = 'apps.Protos_pb2'
  # @@protoc_insertion_point(class_scope:com.mammut.communication.transducers.Issue)
  ))
_sym_db.RegisterMessage(Issue)
_sym_db.RegisterMessage(Issue.ConversationClosure)
_sym_db.RegisterMessage(Issue.ConversationClosure.GraphTransverseValuePair)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\006Protos'))
# @@protoc_insertion_point(module_scope)
