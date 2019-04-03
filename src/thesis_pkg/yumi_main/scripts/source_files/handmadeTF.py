#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.
#!/usr/bin/env python
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import sys
sys.path.insert(0, '/home/casch/yumi_depends_ws/src/thesis_pkg/yumi_main/scripts/project')
from thesis_library import *


#from my turtlebot code
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty
from math import pow,atan2,sqrt,radians



def publish_transforms(trans,rot):

    br = tf2_ros.TransformBroadcaster()

    t10 = geometry_msgs.msg.TransformStamped()
    t10.header.stamp = rospy.Time.now()
    t10.header.frame_id = "world"
    t10.child_frame_id = "camera_link"
    t10.transform.translation.x = trans[0]
    t10.transform.translation.y = trans[1]
    t10.transform.translation.z = trans[2]

    t10.transform.rotation.x = rot[0]
    t10.transform.rotation.y = rot[1]
    t10.transform.rotation.z = rot[2]
    t10.transform.rotation.w = rot[3]
    br.sendTransform(t10)

def world_yumiTCP_callback(msg):
    print('----------------------')
    print('world_yumiTCP_callback')
    pose_world_tcp = Point(0.0,0.0,0.0)
    #print(msg)
    pose_world_tcp.x=msg.position.x
    pose_world_tcp.y=msg.position.y
    pose_world_tcp.z=msg.position.z

    orientation_data=msg.orientation
    quaternion=[orientation_data.x,orientation_data.y,orientation_data.z,orientation_data.w]
    print('pose_world_tcp:')
    print(pose_world_tcp)
    print('quaternion:')
    print(quaternion)

def yumiTCP_camera_callback(msg):
    print('----------------------')
    print('yumiTCP_camera_callback')
    pose_world_tcp = Point(0.0,0.0,0.0)
    #print(msg)
    pose_world_tcp.x=msg.position.x
    pose_world_tcp.y=msg.position.y
    pose_world_tcp.z=msg.position.z

    orientation_data=msg.orientation
    quaternion=[orientation_data.x,orientation_data.y,orientation_data.z,orientation_data.w]
    print('pose_world_tcp:')
    print(pose_world_tcp)
    print('quaternion:')
    print(quaternion)

if __name__ == '__main__':
    rospy.init_node('handmadeTF')




    sub_1 = rospy.Subscriber('/pose_world_yumi_tcp', Pose, world_yumiTCP_callback)
    sub_1 = rospy.Subscriber('/pose_yumi_tcp_camera', Pose, yumiTCP_camera_callback)


    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        print('do something here...')
        rate.sleep()
