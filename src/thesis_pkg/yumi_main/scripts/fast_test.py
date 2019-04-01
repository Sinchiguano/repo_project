#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

"""

"""
# import sys
# sys.path.insert(0, '/home/casch/yumi_depends_ws/src/thesis_pkg/yumi_main/scripts/project')
# from yumi_lib import *

# from yumi_class import MoveGroup,all_close,measurements
from yumipy import YuMiRobot


# starting the robot interface
y = YuMiRobot()

left_state = y.left.get_state()
#right_state = y.right.get_state()

print('left_state:',left_state)
print('-----')
#print('right_state:',right_state)


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
