# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bosdyn/api/time_sync_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bosdyn.api import time_sync_pb2 as bosdyn_dot_api_dot_time__sync__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bosdyn/api/time_sync_service.proto',
  package='bosdyn.api',
  syntax='proto3',
  serialized_pb=_b('\n\"bosdyn/api/time_sync_service.proto\x12\nbosdyn.api\x1a\x1a\x62osdyn/api/time_sync.proto2l\n\x0fTimeSyncService\x12Y\n\x0eTimeSyncUpdate\x12!.bosdyn.api.TimeSyncUpdateRequest\x1a\".bosdyn.api.TimeSyncUpdateResponse\"\x00\x42\x16\x42\x14TimeSyncServiceProtob\x06proto3')
  ,
  dependencies=[bosdyn_dot_api_dot_time__sync__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\024TimeSyncServiceProto'))

_TIMESYNCSERVICE = _descriptor.ServiceDescriptor(
  name='TimeSyncService',
  full_name='bosdyn.api.TimeSyncService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=78,
  serialized_end=186,
  methods=[
  _descriptor.MethodDescriptor(
    name='TimeSyncUpdate',
    full_name='bosdyn.api.TimeSyncService.TimeSyncUpdate',
    index=0,
    containing_service=None,
    input_type=bosdyn_dot_api_dot_time__sync__pb2._TIMESYNCUPDATEREQUEST,
    output_type=bosdyn_dot_api_dot_time__sync__pb2._TIMESYNCUPDATERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TIMESYNCSERVICE)

DESCRIPTOR.services_by_name['TimeSyncService'] = _TIMESYNCSERVICE

# @@protoc_insertion_point(module_scope)
