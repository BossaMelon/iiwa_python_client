# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_iiwa.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_iiwa.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\023io.grpc.iiwaServiceP\001'),
  serialized_pb=_b('\n\x0fgrpc_iiwa.proto\"\x1e\n\x0brobot_reply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x10\n\x0epython_request\"b\n\x1erobot_cartesian_position_reply\x12\t\n\x01X\x18\x01 \x01(\x01\x12\t\n\x01Y\x18\x02 \x01(\x01\x12\t\n\x01Z\x18\x03 \x01(\x01\x12\t\n\x01\x41\x18\x04 \x01(\x01\x12\t\n\x01\x42\x18\x05 \x01(\x01\x12\t\n\x01\x43\x18\x06 \x01(\x01\"p\n\x1arobot_joint_position_reply\x12\n\n\x02\x41\x31\x18\x01 \x01(\x01\x12\n\n\x02\x41\x32\x18\x02 \x01(\x01\x12\n\n\x02\x41\x33\x18\x03 \x01(\x01\x12\n\n\x02\x41\x34\x18\x04 \x01(\x01\x12\n\n\x02\x41\x35\x18\x05 \x01(\x01\x12\n\n\x02\x41\x36\x18\x06 \x01(\x01\x12\n\n\x02\x41\x37\x18\x07 \x01(\x01\"d\n!python_cartesian_position_request\x12\t\n\x01X\x18\x01 \x01(\x01\x12\t\n\x01Y\x18\x02 \x01(\x01\x12\t\n\x01Z\x18\x03 \x01(\x01\x12\x10\n\x08velocity\x18\x04 \x01(\x01\x12\x0c\n\x04mode\x18\x05 \x01(\x08\"\x81\x01\n\x1dpython_cartesian_pose_request\x12\t\n\x01X\x18\x01 \x01(\x01\x12\t\n\x01Y\x18\x02 \x01(\x01\x12\t\n\x01Z\x18\x03 \x01(\x01\x12\t\n\x01\x41\x18\x04 \x01(\x01\x12\t\n\x01\x42\x18\x05 \x01(\x01\x12\t\n\x01\x43\x18\x06 \x01(\x01\x12\x10\n\x08velocity\x18\x07 \x01(\x01\x12\x0c\n\x04mode\x18\x08 \x01(\x08\"F\n\x0f\x66orce_condition\x12\r\n\x05\x66orce\x18\x01 \x01(\x01\x12\x12\n\nz_distance\x18\x02 \x01(\x01\x12\x10\n\x08velocity\x18\x03 \x01(\x01\x32\x92\x03\n\x0biiwaService\x12J\n\x14\x61skCartesianPosition\x12\x0f.python_request\x1a\x1f.robot_cartesian_position_reply\"\x00\x12\x42\n\x10\x61skJointPosition\x12\x0f.python_request\x1a\x1b.robot_joint_position_reply\"\x00\x12:\n\x04move\x12\".python_cartesian_position_request\x1a\x0c.robot_reply\"\x00\x12G\n\x15move_with_orientation\x12\x1e.python_cartesian_pose_request\x1a\x0c.robot_reply\"\x00\x12-\n\tauto_down\x12\x10.force_condition\x1a\x0c.robot_reply\"\x00\x12?\n\rhold_position\x12\x1e.python_cartesian_pose_request\x1a\x0c.robot_reply\"\x00\x42\x17\n\x13io.grpc.iiwaServiceP\x01\x62\x06proto3')
)




_ROBOT_REPLY = _descriptor.Descriptor(
  name='robot_reply',
  full_name='robot_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='robot_reply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=19,
  serialized_end=49,
)


_PYTHON_REQUEST = _descriptor.Descriptor(
  name='python_request',
  full_name='python_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=51,
  serialized_end=67,
)


_ROBOT_CARTESIAN_POSITION_REPLY = _descriptor.Descriptor(
  name='robot_cartesian_position_reply',
  full_name='robot_cartesian_position_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='X', full_name='robot_cartesian_position_reply.X', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Y', full_name='robot_cartesian_position_reply.Y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Z', full_name='robot_cartesian_position_reply.Z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A', full_name='robot_cartesian_position_reply.A', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='B', full_name='robot_cartesian_position_reply.B', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='C', full_name='robot_cartesian_position_reply.C', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=69,
  serialized_end=167,
)


_ROBOT_JOINT_POSITION_REPLY = _descriptor.Descriptor(
  name='robot_joint_position_reply',
  full_name='robot_joint_position_reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='A1', full_name='robot_joint_position_reply.A1', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A2', full_name='robot_joint_position_reply.A2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A3', full_name='robot_joint_position_reply.A3', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A4', full_name='robot_joint_position_reply.A4', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A5', full_name='robot_joint_position_reply.A5', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A6', full_name='robot_joint_position_reply.A6', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A7', full_name='robot_joint_position_reply.A7', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=169,
  serialized_end=281,
)


_PYTHON_CARTESIAN_POSITION_REQUEST = _descriptor.Descriptor(
  name='python_cartesian_position_request',
  full_name='python_cartesian_position_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='X', full_name='python_cartesian_position_request.X', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Y', full_name='python_cartesian_position_request.Y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Z', full_name='python_cartesian_position_request.Z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='python_cartesian_position_request.velocity', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='python_cartesian_position_request.mode', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=283,
  serialized_end=383,
)


_PYTHON_CARTESIAN_POSE_REQUEST = _descriptor.Descriptor(
  name='python_cartesian_pose_request',
  full_name='python_cartesian_pose_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='X', full_name='python_cartesian_pose_request.X', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Y', full_name='python_cartesian_pose_request.Y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Z', full_name='python_cartesian_pose_request.Z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A', full_name='python_cartesian_pose_request.A', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='B', full_name='python_cartesian_pose_request.B', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='C', full_name='python_cartesian_pose_request.C', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='python_cartesian_pose_request.velocity', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mode', full_name='python_cartesian_pose_request.mode', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=386,
  serialized_end=515,
)


_FORCE_CONDITION = _descriptor.Descriptor(
  name='force_condition',
  full_name='force_condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='force', full_name='force_condition.force', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z_distance', full_name='force_condition.z_distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='velocity', full_name='force_condition.velocity', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=517,
  serialized_end=587,
)

DESCRIPTOR.message_types_by_name['robot_reply'] = _ROBOT_REPLY
DESCRIPTOR.message_types_by_name['python_request'] = _PYTHON_REQUEST
DESCRIPTOR.message_types_by_name['robot_cartesian_position_reply'] = _ROBOT_CARTESIAN_POSITION_REPLY
DESCRIPTOR.message_types_by_name['robot_joint_position_reply'] = _ROBOT_JOINT_POSITION_REPLY
DESCRIPTOR.message_types_by_name['python_cartesian_position_request'] = _PYTHON_CARTESIAN_POSITION_REQUEST
DESCRIPTOR.message_types_by_name['python_cartesian_pose_request'] = _PYTHON_CARTESIAN_POSE_REQUEST
DESCRIPTOR.message_types_by_name['force_condition'] = _FORCE_CONDITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

robot_reply = _reflection.GeneratedProtocolMessageType('robot_reply', (_message.Message,), {
  'DESCRIPTOR' : _ROBOT_REPLY,
  '__module__' : 'grpc_iiwa_pb2'
  # @@protoc_insertion_point(class_scope:robot_reply)
  })
_sym_db.RegisterMessage(robot_reply)

python_request = _reflection.GeneratedProtocolMessageType('python_request', (_message.Message,), {
  'DESCRIPTOR' : _PYTHON_REQUEST,
  '__module__' : 'grpc_iiwa_pb2'
  # @@protoc_insertion_point(class_scope:python_request)
  })
_sym_db.RegisterMessage(python_request)

robot_cartesian_position_reply = _reflection.GeneratedProtocolMessageType('robot_cartesian_position_reply', (_message.Message,), {
  'DESCRIPTOR' : _ROBOT_CARTESIAN_POSITION_REPLY,
  '__module__' : 'grpc_iiwa_pb2'
  # @@protoc_insertion_point(class_scope:robot_cartesian_position_reply)
  })
_sym_db.RegisterMessage(robot_cartesian_position_reply)

robot_joint_position_reply = _reflection.GeneratedProtocolMessageType('robot_joint_position_reply', (_message.Message,), {
  'DESCRIPTOR' : _ROBOT_JOINT_POSITION_REPLY,
  '__module__' : 'grpc_iiwa_pb2'
  # @@protoc_insertion_point(class_scope:robot_joint_position_reply)
  })
_sym_db.RegisterMessage(robot_joint_position_reply)

python_cartesian_position_request = _reflection.GeneratedProtocolMessageType('python_cartesian_position_request', (_message.Message,), {
  'DESCRIPTOR' : _PYTHON_CARTESIAN_POSITION_REQUEST,
  '__module__' : 'grpc_iiwa_pb2'
  # @@protoc_insertion_point(class_scope:python_cartesian_position_request)
  })
_sym_db.RegisterMessage(python_cartesian_position_request)

python_cartesian_pose_request = _reflection.GeneratedProtocolMessageType('python_cartesian_pose_request', (_message.Message,), {
  'DESCRIPTOR' : _PYTHON_CARTESIAN_POSE_REQUEST,
  '__module__' : 'grpc_iiwa_pb2'
  # @@protoc_insertion_point(class_scope:python_cartesian_pose_request)
  })
_sym_db.RegisterMessage(python_cartesian_pose_request)

force_condition = _reflection.GeneratedProtocolMessageType('force_condition', (_message.Message,), {
  'DESCRIPTOR' : _FORCE_CONDITION,
  '__module__' : 'grpc_iiwa_pb2'
  # @@protoc_insertion_point(class_scope:force_condition)
  })
_sym_db.RegisterMessage(force_condition)


DESCRIPTOR._options = None

_IIWASERVICE = _descriptor.ServiceDescriptor(
  name='iiwaService',
  full_name='iiwaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=590,
  serialized_end=992,
  methods=[
  _descriptor.MethodDescriptor(
    name='askCartesianPosition',
    full_name='iiwaService.askCartesianPosition',
    index=0,
    containing_service=None,
    input_type=_PYTHON_REQUEST,
    output_type=_ROBOT_CARTESIAN_POSITION_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='askJointPosition',
    full_name='iiwaService.askJointPosition',
    index=1,
    containing_service=None,
    input_type=_PYTHON_REQUEST,
    output_type=_ROBOT_JOINT_POSITION_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='move',
    full_name='iiwaService.move',
    index=2,
    containing_service=None,
    input_type=_PYTHON_CARTESIAN_POSITION_REQUEST,
    output_type=_ROBOT_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='move_with_orientation',
    full_name='iiwaService.move_with_orientation',
    index=3,
    containing_service=None,
    input_type=_PYTHON_CARTESIAN_POSE_REQUEST,
    output_type=_ROBOT_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='auto_down',
    full_name='iiwaService.auto_down',
    index=4,
    containing_service=None,
    input_type=_FORCE_CONDITION,
    output_type=_ROBOT_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='hold_position',
    full_name='iiwaService.hold_position',
    index=5,
    containing_service=None,
    input_type=_PYTHON_CARTESIAN_POSE_REQUEST,
    output_type=_ROBOT_REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IIWASERVICE)

DESCRIPTOR.services_by_name['iiwaService'] = _IIWASERVICE

# @@protoc_insertion_point(module_scope)
