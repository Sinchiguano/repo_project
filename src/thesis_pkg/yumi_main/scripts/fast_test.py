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




moves_deg = np.array([[-81.63, -73.53, 50.08, -2.31, -48.69, -83.33, 92.82],
                    [-52.0, -76.14, 47.96, -15.87, -18.56, -69.86, 81.43],
                    [-43.06, -76.55, 56.06, 25.05, -18.75, -100.12, 94.96],
                    [-36.14, -81.51, 62.48, -21.44, -15.48, -67.83, 74.02],
                    [-86.28, -66.29, 43.21, -12.32, -45.17, -85.41, 83.62],
                    [-110.32, -47.88, 32.18, -42.41, -80.97, -83.83, 92.88],
                    [-82.88, -52.2, 40.18, -43.11, -71.83, -73.91, 75.19]])
#[-129.51, -40.42, -5.51, 28.89, -78.44, -153.85, 160.52]

#setting the hand of the robot
#tool_cesar_cal = RigidTransform(np.array([[ 0.,  0.,  1.],[ 0.,  1.,  0.],[-1.,  0.,  0.]]), np.array([0, 0.035, 0.1892]))

tool_cesar_cal = RigidTransform(np.array([[0.0007963, -0.0000000,  0.9999997],
                                        [ 0.0015927, -0.9999987, -0.0000013],
                                        [ 0.9999984,  0.0015927, -0.0007963]]), np.array([0, 0.035, 0.1892]))




g_index_last_move = 0

def move(yumi_robot):

    global g_index_last_move
    global moves_deg

    #Object that encapsulates a yumi arm joint angle configuration.
    moves = [YuMiState(p) for p in moves_deg]

    g_index_last_move = (g_index_last_move + 1) % len(moves)

    yumi_robot.left.goto_state(moves[g_index_last_move],wait_for_res=False)


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

    rospy.init_node('tcp_tf', anonymous=True)
    br = tf2_ros.TransformBroadcaster()

    # starting the robot interface
    y = YuMiRobot(arm_type='remote')

    global tool_cesar_cal
    y.left.set_tool(tool_cesar_cal)
    rate = rospy.Rate(10)

    # pose = y.left.get_state(raw_res=False)
    # print(pose)
    # exit(0)

    while (True):

        pose = y.left.get_pose(raw_res=False)

        print('translation')
        print(pose.translation)
        #print(pose.rotation)
        print('quaternion')
        print(pose.quaternion)

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
