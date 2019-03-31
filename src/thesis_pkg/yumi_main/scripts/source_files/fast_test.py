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


#pose target
pose_target= y.left.get_pose()
pose_target.translation=[ 0.32355002, -0.03232,     0.10034]
pose_target.rotation=[[-0.73188958, -0.27943025, -0.62149528],
                        [ 0.23113712,  0.75618204, -0.61218001],
                        [ 0.64102518, -0.59169879, -0.48885505]]


y.set_v(25)
y.reset_home()


#y.left.open_gripper(no_wait=False, wait_for_res=True)

# print('information about the left arm!!!')
# pose = y.left.get_pose()
# print(pose.translation)
# print(pose.rotation)
# # y.left.reset()


# move right arm forward by 5cm using goto_pose
# y.left.goto_pose(pose_target)
# y.left.close_gripper(force=5, width=0.0, no_wait=False, wait_for_res=True)




#y.left.reset()


