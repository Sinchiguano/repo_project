#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

"""

"""
import sys
sys.path.insert(0, '/home/casch/yumi_depends_ws/src/thesis_pkg/yumi_main/scripts/project')
from thesis_library import *

# from yumi_class import MoveGroup,all_close,measurements
from yumipy import YuMiRobot
from yumipy import YuMiState
from autolab_core import RigidTransform




# moves_deg = np.array([[-81.63, -73.53, 50.08, -2.31, -48.69, -83.33, 92.82],
#                     [-52.0, -76.14, 47.96, -15.87, -18.56, -69.86, 81.43],
#                     [-43.06, -76.55, 56.06, 25.05, -18.75, -100.12, 94.96],
#                     [-36.14, -81.51, 62.48, -21.44, -15.48, -67.83, 74.02],
#                     [-86.28, -66.29, 43.21, -12.32, -45.17, -85.41, 83.62],
#                     [-110.32, -47.88, 32.18, -42.41, -80.97, -83.83, 92.88],
#                     [-82.88, -52.2, 40.18, -43.11, -71.83, -73.91, 75.19]])

moves_deg = np.array([[-118.83, -106.99, 0.21, 68.64, -16.03, -81.35, 42.61],
                    [-122.66, -99.11, -12.67, 81.03, -12.68, -96.27, 39.75],
                    [-118.22, -104.42, 14.18, 31.72, -25.17, -44.6, 41.04],
                    [-118.78, -95.0, -18.42, 106.49, -7.06, -126.19, 35.77],
                    [-108.27, -106.58, 1.2, 69.36, -6.28, -90.27, 37.11],
                    [-112.79, -104.75, -1.72, 69.43, -8.85, -88.0, 38.16],
                    [-112.79, -104.75, -1.72, 69.43, -8.85, -88.0, 38.16],
                    [-121.92, -101.36, -24.07, 129.62, -17.69, -145.72, 40.5],
                    [-116.35, -105.67, -0.9, 68.06, -12.88, -83.43, 40.57],
                    [-123.22, -103.88, -5.89, 73.88, -17.0, -85.8, 42.66],
                    [-115.78, -99.11, 8.09, 17.54, -19.96, -35.91, 35.19],
                    [-130.46, -92.83, -26.13, 97.0, -14.9, -111.37, 40.55],
                    [-122.44, -90.82, -26.37, 120.9, -8.51, -140.31, 35.86],
                    [-130.67, -99.9, -15.62, 83.18, -19.65, -93.41, 43.71],
                    [-122.44, -90.82, -26.37, 120.9, -8.51, -140.31, 35.86]])

# [-123.17, -98.53, 6.38, 1.24, -43.0, -19.54, 40.32],
# [-113.63, -96.68, 4.57, -19.52, -38.59, -4.68, 31.84],
# [-114.0, -97.23, 15.7, -13.8, -62.93, -9.57, 31.5],
# [-120.01, -85.62, 3.4, -17.61, -79.75, -6.93, 29.19],
# [-102.46, -81.65, -5.6, -38.76, -63.84, 14.46, 24.8],
# [-120.53, -88.07, 10.75, -9.29, -75.58, -49.55, 46.92],
# [-110.47, -74.17, -10.43, -63.78, -58.0, -9.96, 46.22],

tool_cesar_cal = RigidTransform(np.array([[0, 0, 1],
                                          [0, -1, 0],
                                          [1, 0, 0]]), np.array([0, 0.035, 0.1892]))
#home position
home_left=[1.25, -129.84, 29.98, -0.76, 40.78, -5.78, 136.29]


g_timestamp_last_move = 0
g_index_last_move = 0

def move(yumi_robot):
    import time
    global g_index_last_move
    global g_timestamp_last_move

    if (time.time() - g_timestamp_last_move) < 3:
        return

    #Object that encapsulates a yumi arm joint angle configuration.
    moves = [YuMiState(p) for p in moves_deg]

    g_index_last_move = (g_index_last_move + 1) % len(moves)

    yumi_robot.left.goto_state(moves[g_index_last_move],wait_for_res=False)
    g_timestamp_last_move = time.time()


def pose_to_tf(br,pose_translation,pose_quaternion):

    """input in m and rad"""

    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'world'
    t.child_frame_id = 'yumi_tcp'
    t.transform.translation.x = pose_translation[0]
    t.transform.translation.y = pose_translation[1]
    t.transform.translation.z = pose_translation[2]
    t.transform.rotation.w = pose_quaternion[0]
    t.transform.rotation.x = pose_quaternion[1]
    t.transform.rotation.y = pose_quaternion[2]
    t.transform.rotation.z = pose_quaternion[3]
    br.sendTransform(t)

def main():
    global home_left
    rospy.init_node('tcp_tf', anonymous=True)
    br = tf2_ros.TransformBroadcaster()

    # starting the robot interface
    y = YuMiRobot(arm_type='remote')

    global tool_cesar_cal
    y.left.set_tool(tool_cesar_cal)
    rate = rospy.Rate(10)

    state = y.left.get_state(raw_res=False)
    print(state)
    #home_left=YuMiState(home_left)
    #y.left.goto_state(home_left,wait_for_res=False)
    # pose = y.left.get_pose(raw_res=False)
    # print(pose.translation)
    # print(pose.rotation)
    # time.sleep(3)
    # state1=[-134.07, -50.55, -4.95, -64.58, -58.61, 95.96, 134.53]
    # state1=YuMiState(state1)
    # y.left.goto_state(state1,wait_for_res=False)
    #exit(0)

    while (True):

        pose = y.left.get_pose(raw_res=False)

        # print('translation {}'.format(pose.translation))
        # print('quaternion {}'.format(pose.quaternion))
        # print('rotation matrix \n{}'.format(pose.rotation))
        print('moving!!!')
        move(y)
        pose_to_tf(br,pose.translation,pose.quaternion)


        # we should expect to go through the loop 10 times per second
        rate.sleep()
if __name__ == '__main__':
    main()
















    # pose_right = y.right.get_pose()
    # pose_left = y.left.get_pose()
    # print('left_state:')
    # print(pose_left.translation)
    # print('right_state:')
    # print(pose_left.rotation)

    #y.left.goto_state(state, wait_for_res=True)

    #pose target
    # pose_target= y.left.get_pose()
    # pose_target.translation=[ 0.32355002, -0.03232,     0.10034]
    # pose_target.rotation=[[-0.73188958, -0.27943025, -0.62149528],
    #                         [ 0.23113712,  0.75618204, -0.61218001],
    #                         [ 0.64102518, -0.59169879, -0.48885505]]



    # move right arm forward by 5cm using goto_pose
    # y.left.goto_pose(pose_target)
    # y.left.close_gripper(force=5, width=0.0, no_wait=False, wait_for_res=True)
