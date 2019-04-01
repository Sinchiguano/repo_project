#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
import sys
sys.path.insert(0, '/home/casch/yumi_depends_ws/src/thesis_pkg/yumi_main/scripts/project')
from yumi_lib import *
from yumi_class import MoveGroup,all_close,measurements

# #Working range, top view
# x=27.4cm
# y=66.4cm

#Main loop!!!
def main():
    global safeJointPositionR
    global safeJointPositionL
    global gripperR
    global gripperL
    # Drive YuMi end effectors to a desired position (pose_ee), and perform a grasping task with a given effort (grip_effort)
    # Gripper effort: opening if negative, closing if positive, static if zero
    pose_ee = [0.3, 0.15, 0.2, 0.0, 3.14, 3.14]
    #pose_ee = [0.07, 0.07, 0.10, 0.0, 3.14, 3.14]
    grip_effort = -10.0

    home_L_=list()
    home_R_=list()


    counter=0
    while(True):

        counter+=1
        rospy.loginfo("counter: %s",counter)

        #############################################################
        ############################################################

        print "\n============ Press `Enter` to execute a sample movement using a joint state goal ..."
        print "\n============ Press 1 to home, 2 to random or any number to do nothing==>>joint state goal ..."
        raw_input()
        # temp=raw_input()
        # control_=int(temp)
        #
        # print('go_to_joint_goal')
        # print('------------------>>>>>>>>>>>>>>>>>>>')
        # print('right arm ready to move!!!')
        # if control_==1:        print("\n============ Press Enter to open the gripperL ...")
        #     state=yumiL.go_to_joint_state(safeJointPositionL)
        # elif control_==2:
        #     state=yumiL.go_to_joint_state()
        # else:
        #     print('nothing')
        measurements(yumiL)


        time.sleep(3)

        #############################################################


        #
        # print("\n============ Press 1 or 2 to open or to close...gripperL ...")
        # temp=raw_input()
        # control_=int(temp)
        #
        # if (control_==1):
        #     yumiL.pub_gripper.publish(std_msgs.msg.Float64(-5))
        #     rospy.sleep(1)
        # elif(control_==2):
        #     yumiL.pub_gripper.publish(std_msgs.msg.Float64(+5))
        #     rospy.sleep(1)


        ############################################################

        # print "\n============ Press `Enter` to execute a sample movement using a pose goal ..."
        # raw_input()
        # print('go_to_pose_goal')
        # print('------------------------>>>>>>>>>>>>>>>>>>>')
        # print('right arm ready to move!!!')


        # print('i am trying!!!')
        # state=yumiL.go_to_pose_goal(pose_ee)
        # measurements(yumiL)

        #state=False
        # while(not state):
        #     print('i am trying!!!')
        #     state=yumiL.go_to_pose_goal(pose_ee)
        #     measurements(yumiL)
        # print('done!!!')




        # print('go_to_random_pose_goal')
        # print('---------------------->>>>>>>>>>>>>>>>>>>')
        # print('right arm moving!!!')
        # state=False
        # while(not state):
        #     print('i am trying!!!')
        #     state=yumiR.go_to_pose_goal(homeR)##homeL, go to the home position for the right-robot arm
        # print('done!!!')
        # measurements(yumiR)

        # ############################################################
        # ###########################################################


        # print('plan_cartesian_path')
        # raw_input()
        # print('I am working...')
        # yumiL.plan_cartesian_path()
        # measurements(yumiL)

        # measurements(yumiL)
        # measurements(yumiR)


if __name__=='__main__':

    print "============ Press `Enter` to start (press ctrl-d to exit) ......"
    raw_input()
    yumiR=MoveGroup('right_arm',gripperR)
    yumiL=MoveGroup('left_arm',gripperL)


    measurements(yumiL)
    #measurements(yumiR)

    main()
