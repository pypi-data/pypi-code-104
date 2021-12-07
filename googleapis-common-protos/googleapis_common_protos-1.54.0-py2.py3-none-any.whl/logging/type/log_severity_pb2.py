# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/logging/type/log_severity.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/logging/type/log_severity.proto",
    package="google.logging.type",
    syntax="proto3",
    serialized_options=b"\n\027com.google.logging.typeB\020LogSeverityProtoP\001Z8google.golang.org/genproto/googleapis/logging/type;ltype\252\002\031Google.Cloud.Logging.Type\312\002\031Google\\Cloud\\Logging\\Type",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n&google/logging/type/log_severity.proto\x12\x13google.logging.type\x1a\x1cgoogle/api/annotations.proto*\x82\x01\n\x0bLogSeverity\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\t\n\x05\x44\x45\x42UG\x10\x64\x12\t\n\x04INFO\x10\xc8\x01\x12\x0b\n\x06NOTICE\x10\xac\x02\x12\x0c\n\x07WARNING\x10\x90\x03\x12\n\n\x05\x45RROR\x10\xf4\x03\x12\r\n\x08\x43RITICAL\x10\xd8\x04\x12\n\n\x05\x41LERT\x10\xbc\x05\x12\x0e\n\tEMERGENCY\x10\xa0\x06\x42\x9f\x01\n\x17\x63om.google.logging.typeB\x10LogSeverityProtoP\x01Z8google.golang.org/genproto/googleapis/logging/type;ltype\xaa\x02\x19Google.Cloud.Logging.Type\xca\x02\x19Google\\Cloud\\Logging\\Typeb\x06proto3",
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)

_LOGSEVERITY = _descriptor.EnumDescriptor(
    name="LogSeverity",
    full_name="google.logging.type.LogSeverity",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="DEFAULT",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DEBUG",
            index=1,
            number=100,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INFO",
            index=2,
            number=200,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NOTICE",
            index=3,
            number=300,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="WARNING",
            index=4,
            number=400,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ERROR",
            index=5,
            number=500,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CRITICAL",
            index=6,
            number=600,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ALERT",
            index=7,
            number=700,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMERGENCY",
            index=8,
            number=800,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=94,
    serialized_end=224,
)
_sym_db.RegisterEnumDescriptor(_LOGSEVERITY)

LogSeverity = enum_type_wrapper.EnumTypeWrapper(_LOGSEVERITY)
DEFAULT = 0
DEBUG = 100
INFO = 200
NOTICE = 300
WARNING = 400
ERROR = 500
CRITICAL = 600
ALERT = 700
EMERGENCY = 800


DESCRIPTOR.enum_types_by_name["LogSeverity"] = _LOGSEVERITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
