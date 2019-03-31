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

#from yumipy
from yumipy import YuMiArm_ROS #single arm over ROS
from yumipy import YuMiRobot #both arms
from yumipy import YuMiArm #single arm over ethernet
#from yumipy import YuMiSubcriber # retrieve pose or state of the robot



def print_pose_state(sub):
    '''Streaming the whole information when it comes to the yumi robot'''
    sub.start()
    left_pose = sub.left.get_pose()
    right_pose = sub.right.get_pose()
    print('left pose {}'.format(left_pose))
    print('right pose {}'.format(right_pose))

    left_state = sub.left.get_state()
    right_state = sub.right.get_state()
    print('left state {}'.format(left_state))
    print('right state {}'.format(right_state))
    sub.stop()
    
    return  left_pose,right_pose

def publish_transforms(br,left,right):

    t2 = geometry_msgs.msg.TransformStamped()
    t2.header.stamp = rospy.Time.now()
    t2.header.frame_id = "world"
    t2.child_frame_id = "base"
    t2.transform.translation.x = 1.0*0.0
    t2.transform.translation.y = 1.0*0.0
    t2.transform.translation.z = 1.0*0.0
    #q2 = tf.transformations.quaternion_from_euler(0,0,0)
    t2.transform.rotation.x = q2[0]
    t2.transform.rotation.y = q2[1]
    t2.transform.rotation.z = q2[2]
    t2.transform.rotation.w = q2[3]
    br.sendTransform(t2)


    # t2 = geometry_msgs.msg.TransformStamped()
    # t2.header.stamp = rospy.Time.now()
    # t2.header.frame_id = "base"
    # t2.child_frame_id = "left"
    # t2.transform.translation.x = 1.0*0.0
    # t2.transform.translation.y = 1.0*0.0
    # t2.transform.translation.z = 1.0*0.0
    # q2 = tf.transformations.quaternion_from_euler(0,0,0)
    # t2.transform.rotation.x = q2[0]
    # t2.transform.rotation.y = q2[1]
    # t2.transform.rotation.z = q2[2]
    # t2.transform.rotation.w = q2[3]
    # br.sendTransform(t2)



    # t1 = geometry_msgs.msg.TransformStamped()
    # t1.header.stamp = rospy.Time.now()
    # t1.header.frame_id = "left"
    # #t1.header.frame_id = "yumi_link_7_l"
    # t1.child_frame_id = "target"
    # t1.transform.translation.x = 0.0
    # t1.transform.translation.y = 0.035
    # t1.transform.translation.z = 0.1892


    # t1.transform.rotation.x = -0.7071
    # t1.transform.rotation.y = 0.0
    # t1.transform.rotation.z = -0.7071
    # t1.transform.rotation.w = 0
    # br.sendTransform(t1)


def main():



    br = tf2_ros.TransformBroadcaster()

    rate = rospy.Rate(10) # 10hz

    counter=0
    while(True):

        counter+=1
        rospy.loginfo("counter: %s",counter)


        print "\n============ Press 1 to go @Home_Position , 2 to go @DesiredPosition or any number to continue--->>joint state goal ..."
        raw_input()
        temp=raw_input()
        control_=int(temp)

        if control_==1:
            #yumiL.reset_home(wait_for_res=True)
            #yumiR.reset_home(wait_for_res=True)
            yumiArms.left.reset_home()
            yumiArms.right.reset_home()

        elif control_==2:
            yumiArms.start()
            
            #right!!!
            # getting the current pose of the right end effector
            pose =yumiArms.right.get_pose()
            # move right arm forward by 5cm using goto_pose
            pose.translation[0] += 0.05
            yumiArms.right.goto_pose(pose, linear=True, relative=False, wait_for_res=True)


            #left!!!
            # getting the current pose of the right end effector
            pose =yumiArms.left.get_pose()
            # move right arm forward by 5cm using goto_pose
            pose.translation[0] += 0.05
            yumiArms.left.goto_pose(pose, linear=True, relative=False, wait_for_res=True)

            yumiArms.stop()
        else:
            print('do nothing')



        # left_pose,right_pose=print_pose_state(sub_pose_state)
        # print('//-----left_pose')
        # print(left_pose)
        # print(left_pose.quaternion)
        # print(left_pose.position)

        print("\n============ Press 1 to open or 2 to close the gripper...")
        temp=raw_input()
        control_=int(temp)

        if (control_==1):
            yumiArms.left.open_gripper(no_wait=False, wait_for_res=True)
            yumiArms.right.open_gripper(no_wait=False, wait_for_res=True)
            
        elif(control_==2):
            yumiArms.left.close_gripper(force=5, width=0.0, no_wait=False, wait_for_res=True)
            yumiArms.right.close_gripper(force=5, width=0.0, no_wait=False, wait_for_res=True)

        #publish_transforms(br,left_pose,right_pose)
           




if __name__=='__main__':

    yumiR=YuMiArm_ROS(arm_service='left_arm')
    # yumiL=YuMiArm_ROS(arm_service='right_arm')
    #sub_pose_state = YuMiSubcriber()
    
    yumiArms=YuMiRobot(arm_type='remote')

    # #Set speed for both arms using n as the speed number.
    # yumiR.set_v(25)
    # yumiL.set_v(25)

    #yumiArms.set_v(25)


    #home positition
    yumiL.reset_home(wait_for_res=True)
    yumiR.reset_home(wait_for_res=True)

    #both arms to home position
    # yumiArms.left.reset_home()
    # yumiArms.right.reset_home()

    #set_tool(pose, wait_for_res=True)
    exit(0)
    main()




# ##############################
# # getting the current joint state of the right end effector
# state=y.right.get_state(raw_res=False)

# #Check if a given pose is reachable
# is_it_goodR=y.right.is_pose_reachable(pose)

# #Commands the YuMi to goto the given state (joint angles)
# goto_state(state, wait_for_res=True)

# #Opens the gripper to the target_width
# open_gripper(no_wait=False, wait_for_res=True)


# #Closes the gripper as close to 0 as possible with maximum force.
# close_gripper(force=5, width=0.0, no_wait=False, wait_for_res=True)

# #Resets the arm to home using joints
# reset_home(wait_for_res=True)

