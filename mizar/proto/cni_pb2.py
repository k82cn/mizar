# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mizar/proto/cni.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mizar/proto/cni.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15mizar/proto/cni.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x15\n\x05PodId\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x8a\x01\n\x03Pod\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tveth_name\x18\x02 \x01(\t\x12\x0b\n\x03mac\x18\x03 \x01(\t\x12\r\n\x05netns\x18\x04 \x01(\t\x12\n\n\x02ip\x18\x05 \x01(\t\x12\x0e\n\x06prefix\x18\x06 \x01(\t\x12\n\n\x02gw\x18\x07 \x01(\t\x12\x1e\n\x08provider\x18\x08 \x01(\x0e\x32\x0c.PodProvider\"p\n\rCniParameters\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontainer_id\x18\x02 \x01(\t\x12\x14\n\x0ck8s_pod_name\x18\x03 \x01(\t\x12\r\n\x05netns\x18\x04 \x01(\t\x12\x13\n\x0b\x63ni_version\x18\x05 \x01(\t\"+\n\nCniResults\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05*\"\n\x0bPodProvider\x12\x07\n\x03K8S\x10\x00\x12\n\n\x06\x41RKTOS\x10\x01\x32\x88\x01\n\nCniService\x12(\n\x06\x41\x64\x64Pod\x12\x04.Pod\x1a\x16.google.protobuf.Empty\"\x00\x12*\n\x06\x44\x65lPod\x12\x06.PodId\x1a\x16.google.protobuf.Empty\"\x00\x12$\n\x03\x43ni\x12\x0e.CniParameters\x1a\x0b.CniResults\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_PODPROVIDER = _descriptor.EnumDescriptor(
  name='PodProvider',
  full_name='PodProvider',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='K8S', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARKTOS', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=377,
  serialized_end=411,
)
_sym_db.RegisterEnumDescriptor(_PODPROVIDER)

PodProvider = enum_type_wrapper.EnumTypeWrapper(_PODPROVIDER)
K8S = 0
ARKTOS = 1



_PODID = _descriptor.Descriptor(
  name='PodId',
  full_name='PodId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PodId.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=54,
  serialized_end=75,
)


_POD = _descriptor.Descriptor(
  name='Pod',
  full_name='Pod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Pod.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='veth_name', full_name='Pod.veth_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mac', full_name='Pod.mac', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='netns', full_name='Pod.netns', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='Pod.ip', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prefix', full_name='Pod.prefix', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gw', full_name='Pod.gw', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='Pod.provider', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=78,
  serialized_end=216,
)


_CNIPARAMETERS = _descriptor.Descriptor(
  name='CniParameters',
  full_name='CniParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='CniParameters.command', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='container_id', full_name='CniParameters.container_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='k8s_pod_name', full_name='CniParameters.k8s_pod_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='netns', full_name='CniParameters.netns', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cni_version', full_name='CniParameters.cni_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=218,
  serialized_end=330,
)


_CNIRESULTS = _descriptor.Descriptor(
  name='CniResults',
  full_name='CniResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='CniResults.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='CniResults.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=332,
  serialized_end=375,
)

_POD.fields_by_name['provider'].enum_type = _PODPROVIDER
DESCRIPTOR.message_types_by_name['PodId'] = _PODID
DESCRIPTOR.message_types_by_name['Pod'] = _POD
DESCRIPTOR.message_types_by_name['CniParameters'] = _CNIPARAMETERS
DESCRIPTOR.message_types_by_name['CniResults'] = _CNIRESULTS
DESCRIPTOR.enum_types_by_name['PodProvider'] = _PODPROVIDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PodId = _reflection.GeneratedProtocolMessageType('PodId', (_message.Message,), {
  'DESCRIPTOR' : _PODID,
  '__module__' : 'mizar.proto.cni_pb2'
  # @@protoc_insertion_point(class_scope:PodId)
  })
_sym_db.RegisterMessage(PodId)

Pod = _reflection.GeneratedProtocolMessageType('Pod', (_message.Message,), {
  'DESCRIPTOR' : _POD,
  '__module__' : 'mizar.proto.cni_pb2'
  # @@protoc_insertion_point(class_scope:Pod)
  })
_sym_db.RegisterMessage(Pod)

CniParameters = _reflection.GeneratedProtocolMessageType('CniParameters', (_message.Message,), {
  'DESCRIPTOR' : _CNIPARAMETERS,
  '__module__' : 'mizar.proto.cni_pb2'
  # @@protoc_insertion_point(class_scope:CniParameters)
  })
_sym_db.RegisterMessage(CniParameters)

CniResults = _reflection.GeneratedProtocolMessageType('CniResults', (_message.Message,), {
  'DESCRIPTOR' : _CNIRESULTS,
  '__module__' : 'mizar.proto.cni_pb2'
  # @@protoc_insertion_point(class_scope:CniResults)
  })
_sym_db.RegisterMessage(CniResults)



_CNISERVICE = _descriptor.ServiceDescriptor(
  name='CniService',
  full_name='CniService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=414,
  serialized_end=550,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddPod',
    full_name='CniService.AddPod',
    index=0,
    containing_service=None,
    input_type=_POD,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DelPod',
    full_name='CniService.DelPod',
    index=1,
    containing_service=None,
    input_type=_PODID,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Cni',
    full_name='CniService.Cni',
    index=2,
    containing_service=None,
    input_type=_CNIPARAMETERS,
    output_type=_CNIRESULTS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CNISERVICE)

DESCRIPTOR.services_by_name['CniService'] = _CNISERVICE

# @@protoc_insertion_point(module_scope)