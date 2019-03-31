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


#home positition
yumi_robot.left.reset_home(wait_for_res=True)
yumi_robot.right.reset_home(wait_for_res=True)




moves_deg = np.array([[-28.3949,-123.008,65.246,-1.95917,72.5597,-159.099, 40.236],
            [-56.8142,-123.004,66.0196,5.00501,72.9616,-159.100, 42.4112],
            [-56.8148,-123.005,72.4107,-1.95587,68.8482,-164.221,42.4142],
            [-44.6196,-123.004,48.6355,-1.85205,87.7641,-154.035,31.6259]])
tool_cesar_cal = RigidTransform(
    np.array([[ 0.,  0.,  1.],
              [ 0.,  1.,  0.],
              [-1.,  0.,  0.]]),
    np.array([0, 0.035, 0.1892]))


yumi_robot.left.set_tool(tool_cesar_cal)


g_timestamp_last_move = 0
g_index_last_move = 0

print("\n============ Press 1 to open or 2 to close the gripper...")
temp=raw_input()
control_=int(temp)

if (control_==1):
    yumi_robot.left.open_gripper(no_wait=False, wait_for_res=True)
elif(control_==2):
    yumi_robot.left.close_gripper(force=5, width=0.0, no_wait=False, wait_for_res=True)


def move(yumi_robot):
    global g_timestamp_last_move
    global g_index_last_move

    moves = [YuMiState(p) for p in moves_deg]

    if (time.time() - g_timestamp_last_move) < 3:
        return

    g_index_last_move = (g_index_last_move + 1) % len(moves)
    print('Moving to {}'.format(moves[g_index_last_move]))
    yumi_robot.left.goto_state(moves[g_index_last_move])
    g_timestamp_last_move = time.time()


while True:
    #  Wait for next request from client
    message = socket.recv()

    pose = yumi_robot.left.get_pose()

    #  Send reply back to client
    msg = b'{0.translation[0]} {0.translation[1]} {0.translation[2]} {0.quaternion[0]} {0.quaternion[1]} {0.quaternion[2]} {0.quaternion[3]}'.format(pose)
    #print('Sending position {}'.format(msg))
    socket.send(msg)
    move(yumi_robot)
