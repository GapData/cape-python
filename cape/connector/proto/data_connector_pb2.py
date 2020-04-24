# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cape/connector/proto/data_connector.proto

import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf.internal import enum_type_wrapper

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="cape/connector/proto/data_connector.proto",
    package="cape",
    syntax="proto3",
    serialized_options=_b("Z\007.;proto"),
    serialized_pb=_b(
        '\n)cape/connector/proto/data_connector.proto\x12\x04\x63\x61pe\x1a\x1fgoogle/protobuf/timestamp.proto"Q\n\x0cQueryRequest\x12\x13\n\x0b\x64\x61ta_source\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x03\x12\x0e\n\x06offset\x18\x04 \x01(\x03"C\n\x06Record\x12\x1c\n\x06schema\x18\x01 \x01(\x0b\x32\x0c.cape.Schema\x12\x1b\n\x06\x66ields\x18\x02 \x03(\x0b\x32\x0b.cape.Field"\xb9\x01\n\x05\x46ield\x12\x0f\n\x05int32\x18\x01 \x01(\x05H\x00\x12\x0f\n\x05int64\x18\x02 \x01(\x03H\x00\x12/\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\x0f\n\x05\x66loat\x18\x04 \x01(\x02H\x00\x12\x10\n\x06\x64ouble\x18\x05 \x01(\x01H\x00\x12\x10\n\x06string\x18\x06 \x01(\tH\x00\x12\x0f\n\x05\x62ytes\x18\x07 \x01(\x0cH\x00\x12\x0e\n\x04\x62ool\x18\x08 \x01(\x08H\x00\x42\x07\n\x05value"n\n\x06Schema\x12\x13\n\x0b\x64\x61ta_source\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12\x1e\n\x04type\x18\x03 \x01(\x0e\x32\x10.cape.RecordType\x12\x1f\n\x06\x66ields\x18\x04 \x03(\x0b\x32\x0f.cape.FieldInfo"G\n\tFieldInfo\x12\x1e\n\x05\x66ield\x18\x01 \x01(\x0e\x32\x0f.cape.FieldType\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t"\x10\n\x0eVersionRequest"6\n\x0fVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x12\n\nbuild_date\x18\x02 \x01(\t*\x1a\n\nRecordType\x12\x0c\n\x08\x44OCUMENT\x10\x00*\xcf\x03\n\tFieldType\x12\n\n\x06\x42IGINT\x10\x00\x12\x07\n\x03\x42IT\x10\x02\x12\n\n\x06VARBIT\x10\x03\x12\x08\n\x04\x42OOL\x10\x04\x12\x07\n\x03\x42OX\x10\x05\x12\t\n\x05\x42YTEA\x10\x06\x12\x08\n\x04\x43HAR\x10\x07\x12\x0b\n\x07VARCHAR\x10\x08\x12\x08\n\x04\x43IDR\x10\t\x12\n\n\x06\x43IRCLE\x10\n\x12\x08\n\x04\x44\x41TE\x10\x0b\x12\n\n\x06\x44OUBLE\x10\x0c\x12\x08\n\x04INET\x10\r\x12\x07\n\x03INT\x10\x0e\x12\x0c\n\x08INTERVAL\x10\x0f\x12\x08\n\x04JSON\x10\x10\x12\t\n\x05JSONB\x10\x11\x12\x08\n\x04LINE\x10\x12\x12\x08\n\x04LSEG\x10\x13\x12\x0b\n\x07MACADDR\x10\x14\x12\x0c\n\x08MACADDR8\x10\x15\x12\t\n\x05MONEY\x10\x16\x12\x0b\n\x07NUMERIC\x10\x17\x12\x08\n\x04PATH\x10\x18\x12\t\n\x05PGLSN\x10\x19\x12\t\n\x05POINT\x10\x1a\x12\x0b\n\x07POLYGON\x10\x1b\x12\x08\n\x04REAL\x10\x1c\x12\x0c\n\x08SMALLINT\x10\x1d\x12\x08\n\x04TEXT\x10 \x12\x08\n\x04TIME\x10!\x12\n\n\x06TIMETZ\x10"\x12\r\n\tTIMESTAMP\x10#\x12\x0f\n\x0bTIMESTAMPTZ\x10$\x12\x0b\n\x07TSQUERY\x10%\x12\x0c\n\x08TSVECTOR\x10&\x12\x10\n\x0cTXIDSNAPSHOT\x10\'\x12\x08\n\x04UUID\x10(\x12\x07\n\x03XML\x10)2t\n\rDataConnector\x12+\n\x05Query\x12\x12.cape.QueryRequest\x1a\x0c.cape.Record0\x01\x12\x36\n\x07Version\x12\x14.cape.VersionRequest\x1a\x15.cape.VersionResponseB\tZ\x07.;protob\x06proto3'
    ),
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,],
)

_RECORDTYPE = _descriptor.EnumDescriptor(
    name="RecordType",
    full_name="cape.RecordType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="DOCUMENT", index=0, number=0, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=683,
    serialized_end=709,
)
_sym_db.RegisterEnumDescriptor(_RECORDTYPE)

RecordType = enum_type_wrapper.EnumTypeWrapper(_RECORDTYPE)
_FIELDTYPE = _descriptor.EnumDescriptor(
    name="FieldType",
    full_name="cape.FieldType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="BIGINT", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BIT", index=1, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="VARBIT", index=2, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BOOL", index=3, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BOX", index=4, number=5, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BYTEA", index=5, number=6, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CHAR", index=6, number=7, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="VARCHAR", index=7, number=8, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CIDR", index=8, number=9, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CIRCLE", index=9, number=10, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DATE", index=10, number=11, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="DOUBLE", index=11, number=12, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INET", index=12, number=13, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INT", index=13, number=14, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INTERVAL", index=14, number=15, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="JSON", index=15, number=16, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="JSONB", index=16, number=17, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="LINE", index=17, number=18, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="LSEG", index=18, number=19, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MACADDR", index=19, number=20, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MACADDR8", index=20, number=21, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MONEY", index=21, number=22, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="NUMERIC", index=22, number=23, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PATH", index=23, number=24, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="PGLSN", index=24, number=25, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="POINT", index=25, number=26, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="POLYGON", index=26, number=27, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="REAL", index=27, number=28, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SMALLINT", index=28, number=29, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TEXT", index=29, number=32, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TIME", index=30, number=33, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TIMETZ", index=31, number=34, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TIMESTAMP", index=32, number=35, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TIMESTAMPTZ", index=33, number=36, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TSQUERY", index=34, number=37, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TSVECTOR", index=35, number=38, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TXIDSNAPSHOT", index=36, number=39, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="UUID", index=37, number=40, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="XML", index=38, number=41, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=712,
    serialized_end=1175,
)
_sym_db.RegisterEnumDescriptor(_FIELDTYPE)

FieldType = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPE)
DOCUMENT = 0
BIGINT = 0
BIT = 2
VARBIT = 3
BOOL = 4
BOX = 5
BYTEA = 6
CHAR = 7
VARCHAR = 8
CIDR = 9
CIRCLE = 10
DATE = 11
DOUBLE = 12
INET = 13
INT = 14
INTERVAL = 15
JSON = 16
JSONB = 17
LINE = 18
LSEG = 19
MACADDR = 20
MACADDR8 = 21
MONEY = 22
NUMERIC = 23
PATH = 24
PGLSN = 25
POINT = 26
POLYGON = 27
REAL = 28
SMALLINT = 29
TEXT = 32
TIME = 33
TIMETZ = 34
TIMESTAMP = 35
TIMESTAMPTZ = 36
TSQUERY = 37
TSVECTOR = 38
TXIDSNAPSHOT = 39
UUID = 40
XML = 41


_QUERYREQUEST = _descriptor.Descriptor(
    name="QueryRequest",
    full_name="cape.QueryRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="data_source",
            full_name="cape.QueryRequest.data_source",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="query",
            full_name="cape.QueryRequest.query",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="limit",
            full_name="cape.QueryRequest.limit",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="offset",
            full_name="cape.QueryRequest.offset",
            index=3,
            number=4,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=84,
    serialized_end=165,
)


_RECORD = _descriptor.Descriptor(
    name="Record",
    full_name="cape.Record",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="schema",
            full_name="cape.Record.schema",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fields",
            full_name="cape.Record.fields",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=167,
    serialized_end=234,
)


_FIELD = _descriptor.Descriptor(
    name="Field",
    full_name="cape.Field",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="int32",
            full_name="cape.Field.int32",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="int64",
            full_name="cape.Field.int64",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="timestamp",
            full_name="cape.Field.timestamp",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="float",
            full_name="cape.Field.float",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="double",
            full_name="cape.Field.double",
            index=4,
            number=5,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="string",
            full_name="cape.Field.string",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bytes",
            full_name="cape.Field.bytes",
            index=6,
            number=7,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bool",
            full_name="cape.Field.bool",
            index=7,
            number=8,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="value",
            full_name="cape.Field.value",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=237,
    serialized_end=422,
)


_SCHEMA = _descriptor.Descriptor(
    name="Schema",
    full_name="cape.Schema",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="data_source",
            full_name="cape.Schema.data_source",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="cape.Schema.target",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="type",
            full_name="cape.Schema.type",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fields",
            full_name="cape.Schema.fields",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=424,
    serialized_end=534,
)


_FIELDINFO = _descriptor.Descriptor(
    name="FieldInfo",
    full_name="cape.FieldInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="field",
            full_name="cape.FieldInfo.field",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="size",
            full_name="cape.FieldInfo.size",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name",
            full_name="cape.FieldInfo.name",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=536,
    serialized_end=607,
)


_VERSIONREQUEST = _descriptor.Descriptor(
    name="VersionRequest",
    full_name="cape.VersionRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=609,
    serialized_end=625,
)


_VERSIONRESPONSE = _descriptor.Descriptor(
    name="VersionResponse",
    full_name="cape.VersionResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="version",
            full_name="cape.VersionResponse.version",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="build_date",
            full_name="cape.VersionResponse.build_date",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=627,
    serialized_end=681,
)

_RECORD.fields_by_name["schema"].message_type = _SCHEMA
_RECORD.fields_by_name["fields"].message_type = _FIELD
_FIELD.fields_by_name[
    "timestamp"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FIELD.oneofs_by_name["value"].fields.append(_FIELD.fields_by_name["int32"])
_FIELD.fields_by_name["int32"].containing_oneof = _FIELD.oneofs_by_name["value"]
_FIELD.oneofs_by_name["value"].fields.append(_FIELD.fields_by_name["int64"])
_FIELD.fields_by_name["int64"].containing_oneof = _FIELD.oneofs_by_name["value"]
_FIELD.oneofs_by_name["value"].fields.append(_FIELD.fields_by_name["timestamp"])
_FIELD.fields_by_name["timestamp"].containing_oneof = _FIELD.oneofs_by_name["value"]
_FIELD.oneofs_by_name["value"].fields.append(_FIELD.fields_by_name["float"])
_FIELD.fields_by_name["float"].containing_oneof = _FIELD.oneofs_by_name["value"]
_FIELD.oneofs_by_name["value"].fields.append(_FIELD.fields_by_name["double"])
_FIELD.fields_by_name["double"].containing_oneof = _FIELD.oneofs_by_name["value"]
_FIELD.oneofs_by_name["value"].fields.append(_FIELD.fields_by_name["string"])
_FIELD.fields_by_name["string"].containing_oneof = _FIELD.oneofs_by_name["value"]
_FIELD.oneofs_by_name["value"].fields.append(_FIELD.fields_by_name["bytes"])
_FIELD.fields_by_name["bytes"].containing_oneof = _FIELD.oneofs_by_name["value"]
_FIELD.oneofs_by_name["value"].fields.append(_FIELD.fields_by_name["bool"])
_FIELD.fields_by_name["bool"].containing_oneof = _FIELD.oneofs_by_name["value"]
_SCHEMA.fields_by_name["type"].enum_type = _RECORDTYPE
_SCHEMA.fields_by_name["fields"].message_type = _FIELDINFO
_FIELDINFO.fields_by_name["field"].enum_type = _FIELDTYPE
DESCRIPTOR.message_types_by_name["QueryRequest"] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name["Record"] = _RECORD
DESCRIPTOR.message_types_by_name["Field"] = _FIELD
DESCRIPTOR.message_types_by_name["Schema"] = _SCHEMA
DESCRIPTOR.message_types_by_name["FieldInfo"] = _FIELDINFO
DESCRIPTOR.message_types_by_name["VersionRequest"] = _VERSIONREQUEST
DESCRIPTOR.message_types_by_name["VersionResponse"] = _VERSIONRESPONSE
DESCRIPTOR.enum_types_by_name["RecordType"] = _RECORDTYPE
DESCRIPTOR.enum_types_by_name["FieldType"] = _FIELDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryRequest = _reflection.GeneratedProtocolMessageType(
    "QueryRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYREQUEST,
        "__module__": "cape.connector.proto.data_connector_pb2"
        # @@protoc_insertion_point(class_scope:cape.QueryRequest)
    },
)
_sym_db.RegisterMessage(QueryRequest)

Record = _reflection.GeneratedProtocolMessageType(
    "Record",
    (_message.Message,),
    {
        "DESCRIPTOR": _RECORD,
        "__module__": "cape.connector.proto.data_connector_pb2"
        # @@protoc_insertion_point(class_scope:cape.Record)
    },
)
_sym_db.RegisterMessage(Record)

Field = _reflection.GeneratedProtocolMessageType(
    "Field",
    (_message.Message,),
    {
        "DESCRIPTOR": _FIELD,
        "__module__": "cape.connector.proto.data_connector_pb2"
        # @@protoc_insertion_point(class_scope:cape.Field)
    },
)
_sym_db.RegisterMessage(Field)

Schema = _reflection.GeneratedProtocolMessageType(
    "Schema",
    (_message.Message,),
    {
        "DESCRIPTOR": _SCHEMA,
        "__module__": "cape.connector.proto.data_connector_pb2"
        # @@protoc_insertion_point(class_scope:cape.Schema)
    },
)
_sym_db.RegisterMessage(Schema)

FieldInfo = _reflection.GeneratedProtocolMessageType(
    "FieldInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _FIELDINFO,
        "__module__": "cape.connector.proto.data_connector_pb2"
        # @@protoc_insertion_point(class_scope:cape.FieldInfo)
    },
)
_sym_db.RegisterMessage(FieldInfo)

VersionRequest = _reflection.GeneratedProtocolMessageType(
    "VersionRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _VERSIONREQUEST,
        "__module__": "cape.connector.proto.data_connector_pb2"
        # @@protoc_insertion_point(class_scope:cape.VersionRequest)
    },
)
_sym_db.RegisterMessage(VersionRequest)

VersionResponse = _reflection.GeneratedProtocolMessageType(
    "VersionResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _VERSIONRESPONSE,
        "__module__": "cape.connector.proto.data_connector_pb2"
        # @@protoc_insertion_point(class_scope:cape.VersionResponse)
    },
)
_sym_db.RegisterMessage(VersionResponse)


DESCRIPTOR._options = None

_DATACONNECTOR = _descriptor.ServiceDescriptor(
    name="DataConnector",
    full_name="cape.DataConnector",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=1177,
    serialized_end=1293,
    methods=[
        _descriptor.MethodDescriptor(
            name="Query",
            full_name="cape.DataConnector.Query",
            index=0,
            containing_service=None,
            input_type=_QUERYREQUEST,
            output_type=_RECORD,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="Version",
            full_name="cape.DataConnector.Version",
            index=1,
            containing_service=None,
            input_type=_VERSIONREQUEST,
            output_type=_VERSIONRESPONSE,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_DATACONNECTOR)

DESCRIPTOR.services_by_name["DataConnector"] = _DATACONNECTOR

# @@protoc_insertion_point(module_scope)
