# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bosdyn/api/power_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bosdyn.api import power_pb2 as bosdyn_dot_api_dot_power__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bosdyn/api/power_service.proto',
  package='bosdyn.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1e\x62osdyn/api/power_service.proto\x12\nbosdyn.api\x1a\x16\x62osdyn/api/power.proto2\xd0\x01\n\x0cPowerService\x12S\n\x0cPowerCommand\x12\x1f.bosdyn.api.PowerCommandRequest\x1a .bosdyn.api.PowerCommandResponse\"\x00\x12k\n\x14PowerCommandFeedback\x12\'.bosdyn.api.PowerCommandFeedbackRequest\x1a(.bosdyn.api.PowerCommandFeedbackResponse\"\x00\x42\x13\x42\x11PowerServiceProtob\x06proto3')
  ,
  dependencies=[bosdyn_dot_api_dot_power__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\021PowerServiceProto'))

_POWERSERVICE = _descriptor.ServiceDescriptor(
  name='PowerService',
  full_name='bosdyn.api.PowerService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=71,
  serialized_end=279,
  methods=[
  _descriptor.MethodDescriptor(
    name='PowerCommand',
    full_name='bosdyn.api.PowerService.PowerCommand',
    index=0,
    containing_service=None,
    input_type=bosdyn_dot_api_dot_power__pb2._POWERCOMMANDREQUEST,
    output_type=bosdyn_dot_api_dot_power__pb2._POWERCOMMANDRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PowerCommandFeedback',
    full_name='bosdyn.api.PowerService.PowerCommandFeedback',
    index=1,
    containing_service=None,
    input_type=bosdyn_dot_api_dot_power__pb2._POWERCOMMANDFEEDBACKREQUEST,
    output_type=bosdyn_dot_api_dot_power__pb2._POWERCOMMANDFEEDBACKRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_POWERSERVICE)

DESCRIPTOR.services_by_name['PowerService'] = _POWERSERVICE

# @@protoc_insertion_point(module_scope)
