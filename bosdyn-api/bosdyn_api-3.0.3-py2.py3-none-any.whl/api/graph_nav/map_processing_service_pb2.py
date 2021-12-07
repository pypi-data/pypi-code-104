# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bosdyn/api/graph_nav/map_processing_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bosdyn.api.graph_nav import map_processing_pb2 as bosdyn_dot_api_dot_graph__nav_dot_map__processing__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bosdyn/api/graph_nav/map_processing_service.proto',
  package='bosdyn.api.graph_nav',
  syntax='proto3',
  serialized_pb=_b('\n1bosdyn/api/graph_nav/map_processing_service.proto\x12\x14\x62osdyn.api.graph_nav\x1a)bosdyn/api/graph_nav/map_processing.proto2\x81\x02\n\x14MapProcessingService\x12r\n\x0fProcessTopology\x12,.bosdyn.api.graph_nav.ProcessTopologyRequest\x1a-.bosdyn.api.graph_nav.ProcessTopologyResponse\"\x00\x30\x01\x12u\n\x10ProcessAnchoring\x12-.bosdyn.api.graph_nav.ProcessAnchoringRequest\x1a..bosdyn.api.graph_nav.ProcessAnchoringResponse\"\x00\x30\x01\x42\x1b\x42\x19MapProcessingServiceProtob\x06proto3')
  ,
  dependencies=[bosdyn_dot_api_dot_graph__nav_dot_map__processing__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\031MapProcessingServiceProto'))

_MAPPROCESSINGSERVICE = _descriptor.ServiceDescriptor(
  name='MapProcessingService',
  full_name='bosdyn.api.graph_nav.MapProcessingService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=119,
  serialized_end=376,
  methods=[
  _descriptor.MethodDescriptor(
    name='ProcessTopology',
    full_name='bosdyn.api.graph_nav.MapProcessingService.ProcessTopology',
    index=0,
    containing_service=None,
    input_type=bosdyn_dot_api_dot_graph__nav_dot_map__processing__pb2._PROCESSTOPOLOGYREQUEST,
    output_type=bosdyn_dot_api_dot_graph__nav_dot_map__processing__pb2._PROCESSTOPOLOGYRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ProcessAnchoring',
    full_name='bosdyn.api.graph_nav.MapProcessingService.ProcessAnchoring',
    index=1,
    containing_service=None,
    input_type=bosdyn_dot_api_dot_graph__nav_dot_map__processing__pb2._PROCESSANCHORINGREQUEST,
    output_type=bosdyn_dot_api_dot_graph__nav_dot_map__processing__pb2._PROCESSANCHORINGRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAPPROCESSINGSERVICE)

DESCRIPTOR.services_by_name['MapProcessingService'] = _MAPPROCESSINGSERVICE

# @@protoc_insertion_point(module_scope)
