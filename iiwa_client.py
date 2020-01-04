from __future__ import print_function

import time

import dependency
import grpc
import grpc_iiwa_pb2
import grpc_iiwa_pb2_grpc


class lbr_grpc_client:

    def __init__(self, ip="172.31.1.147", port=30009):
        self.ip = ip
        self.port = str(port)
        self.channel = grpc.insecure_channel(self.ip + ":" + self.port)
        self.stub = grpc_iiwa_pb2_grpc.iiwaServiceStub(self.channel)

    def run(self):
        # print(self.ask_home())
        self.move([550, 0, 500])
        print("Current joint Position: " + str(self.ask_joint_position()))
        print("Current Cartesian Position: " + str(self.ask_cartesian_position()))

    def ask_joint_position(self):
        response = self.stub.askJointPosition(grpc_iiwa_pb2.python_request())
        robot_cartesian_position = [response.A1, response.A2, response.A3, response.A4,
                                    response.A5, response.A6, response.A7]
        return robot_cartesian_position

    def ask_cartesian_position(self):
        response = self.stub.askCartesianPosition(grpc_iiwa_pb2.python_request())
        robot_cartesian_position = [response.X, response.Y, response.Z, response.A, response.B, response.C]
        return robot_cartesian_position

    def auto_down(self, force, z_distance, velocity):
        response = self.stub.auto_down(grpc_iiwa_pb2.force_condition(force=force, z_distance=z_distance, velocity=velocity))
        return response.success

    def hold_position(self, cartesian_position, cartesian_orientation, velocity=0.25, mode='lin'):
        if mode == 'lin':
            mode = True
        elif mode == 'ptp':
            mode = False
        else:
            print('mode error,only lin and ptp')
            return


        x = cartesian_position[0]
        y = cartesian_position[1]
        z = cartesian_position[2]
        a = cartesian_orientation[0]
        b = cartesian_orientation[1]
        c = cartesian_orientation[2]

        response = self.stub.hold_position(
                grpc_iiwa_pb2.python_cartesian_pose_request(X=x, Y=y, Z=z, A=a, B=b, C=c, velocity=velocity, mode=mode))

        return response.success


    def move(self, cartesian_position, cartesian_orientation=None, velocity=0.25, mode='lin'):
        if mode == 'lin':
            mode = True
        elif mode == 'ptp':
            mode = False
        else:
            print('mode error,only lin and ptp')
            return

        if cartesian_orientation is None:
            x = cartesian_position[0]
            y = cartesian_position[1]
            z = cartesian_position[2]
            response = self.stub.move(
                grpc_iiwa_pb2.python_cartesian_position_request(X=x, Y=y, Z=z, velocity=velocity, mode=mode))

        else:
            x = cartesian_position[0]
            y = cartesian_position[1]
            z = cartesian_position[2]
            a = cartesian_orientation[0]
            b = cartesian_orientation[1]
            c = cartesian_orientation[2]

            response = self.stub.move_with_orientation(
                grpc_iiwa_pb2.python_cartesian_pose_request(X=x, Y=y, Z=z, A=a, B=b, C=c, velocity=velocity, mode=mode))
        return response.success

    def to_home(self):
        return self.move([550, 0, 500],[-3.141592654,0,3.141592654])



if __name__ == '__main__':
    lbr = lbr_grpc_client()

    print(lbr.ask_cartesian_position())

    # lbr.to_home()
    #
    # lbr.move([500, 100, 300])
    #
    # lbr.to_home()
    #
    # lbr.move([500, 100, 300],mode='ptp', velocity=0.5)
    #
    # lbr.to_home()
    #
    # lbr.move(([500, 100, 300]),[-2.5,0,2.5])
    #
    # lbr.to_home()

    lbr.move([550, 0, 300])
    print(lbr.auto_down(force=4, z_distance=250, velocity=0.1))


    lbr.hold_position(([650, 0, 400]),[-3.141592654,0,3.141592654])











