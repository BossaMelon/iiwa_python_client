from __future__ import print_function

import time

import dependency
import grpc
import grpc_iiwa_pb2
import grpc_iiwa_pb2_grpc


class grpc_client:
    def __init__(self, ip="localhost", port=50051):
        self.ip = ip
        self.port = str(port)
        self.channel = grpc.insecure_channel(self.ip + ":" + self.port)
        self.stub = grpc_iiwa_pb2_grpc.iiwaServiceStub(self.channel)

    def run(self):
        print(self.ask_home())
        print("Current Cartesian Position: " + str(self.ask_joint_position()))
        print("Current Cartesian Position: " + str(self.ask_cartesian_position()))
        self.move([1, 2, 3])

    def ask_home(self):
        response = self.stub.askHome(grpc_iiwa_pb2.python_request())
        return response.success

    def ask_joint_position(self):
        response = self.stub.askJointPosition(grpc_iiwa_pb2.python_request())
        robot_cartesian_position = [response.A1, response.A2, response.A3, response.A4,
                                    response.A5, response.A6, response.A7]
        return robot_cartesian_position

    def ask_cartesian_position(self):
        response = self.stub.askCartesianPosition(grpc_iiwa_pb2.python_request())
        robot_cartesian_position = [response.X, response.Y, response.Z, response.A, response.B, response.C]
        return robot_cartesian_position

    def move(self, cartesian_position):
        x = cartesian_position[0]
        y = cartesian_position[1]
        z = cartesian_position[2]
        response = self.stub.move(grpc_iiwa_pb2.python_cartesian_position_request(X=x, Y=y, Z=z))
        print(response.success)


if __name__ == '__main__':
    grpc = grpc_client("192.168.31.112", 50051)
    for i in range(10):
        grpc.run()
        time.sleep(3)

