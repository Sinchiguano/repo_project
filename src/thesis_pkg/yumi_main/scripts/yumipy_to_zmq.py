#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from autolab_core import RigidTransform
import numpy as np
from yumipy import YuMiRobot
from yumipy import YuMiState
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

yumi_robot = YuMiRobot()


moves_deg = np.array([[-81.63, -73.53, 50.08, -2.31, -48.69, -83.33, 92.82],
                    [-52.0, -76.14, 47.96, -15.87, -18.56, -69.86, 81.43],
                    [-43.06, -76.55, 56.06, 25.05, -18.75, -100.12, 94.96],
                    [-36.14, -81.51, 62.48, -21.44, -15.48, -67.83, 74.02],
                    [-86.28, -66.29, 43.21, -12.32, -45.17, -85.41, 83.62],
                    [-110.32, -47.88, 32.18, -42.41, -80.97, -83.83, 92.88],
                    [-82.88, -52.2, 40.18, -43.11, -71.83, -73.91, 75.19]])



#setting the hand of the robot
tool_cesar_cal = RigidTransform(np.array([[ 0.,  0.,  1.],
                                          [ 0.,  1.,  0.],
                                          [-1.,  0.,  0.]]), np.array([0, 0.035, 0.1892]))
yumi_robot.left.set_tool(tool_cesar_cal)


g_timestamp_last_move = 0
g_index_last_move = 0

def move(yumi_robot):
    global g_timestamp_last_move
    global g_index_last_move

    moves = [YuMiState(p) for p in moves_deg]

    if (time.time() - g_timestamp_last_move) < 3:
        return

    g_index_last_move = (g_index_last_move + 1) % len(moves)
    print('Moving to {}'.format(moves[g_index_last_move]))
    start = time.time()
    yumi_robot.left.goto_state(moves[g_index_last_move])
    g_timestamp_last_move = time.time()
    print('goto_state command took {} s'.format(g_timestamp_last_move - start))

def main():

    # print("\n============ Press 1 to open or 2 to close the gripper...")
    # temp=raw_input()
    # control_=int(temp)

    # if (control_==1):
    #     yumi_robot.left.open_gripper(no_wait=False, wait_for_res=True)
    # elif(control_==2):
    #     yumi_robot.left.close_gripper(force=5, width=0.0, no_wait=False, wait_for_res=True)

    while True:
        #  Wait for next request from client
        message = socket.recv()

        start = time.time()
        pose = yumi_robot.left.get_pose()
        print('get_pose command took {} s'.format(time.time() - start))

        #  Send reply back to client
        msg = b'{0.translation[0]} {0.translation[1]} {0.translation[2]} {0.quaternion[0]} {0.quaternion[1]} {0.quaternion[2]} {0.quaternion[3]}'.format(pose)
        #print('Sending position {}'.format(msg))
        socket.send(msg)
        move(yumi_robot)

if __name__=='__main__':
    main()
