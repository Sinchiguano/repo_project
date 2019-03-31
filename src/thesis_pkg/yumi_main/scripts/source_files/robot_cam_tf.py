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
def publish_transforms(br,trans,rot,trans1,rot1):

    global euler_angles_
    global position_


    t10 = geometry_msgs.msg.TransformStamped()
    t10.header.stamp = rospy.Time.now()
    t10.header.frame_id = "yumi_body"
    t10.child_frame_id = "camera_link"
    t10.transform.translation.x = trans[0]
    t10.transform.translation.y = trans[1]
    t10.transform.translation.z = trans[2]
    
    t10.transform.rotation.x = rot[0]
    t10.transform.rotation.y = rot[1]
    t10.transform.rotation.z = rot[2]
    t10.transform.rotation.w = rot[3]
    br.sendTransform(t10)


    t20 = geometry_msgs.msg.TransformStamped()
    t20.header.stamp = rospy.Time.now()
    t20.header.frame_id = "yumi_body"
    t20.child_frame_id = "target"
    t20.transform.translation.x = trans1[0]
    t20.transform.translation.y = trans1[1]
    t20.transform.translation.z = trans1[2]
    
    t20.transform.rotation.x = rot1[0]
    t20.transform.rotation.y = rot1[1]
    t20.transform.rotation.z = rot1[2]
    t20.transform.rotation.w = rot1[3]
    br.sendTransform(t20)
if __name__ == '__main__':
    rospy.init_node('robot_cam_tf_listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    br = tf2_ros.TransformBroadcaster()
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/yumi_body','/camera_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        try:
            (trans1,rot1) = listener.lookupTransform('/yumi_body','/target', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue


        print('here the transform from world to camera_link frame')
        print(trans)
        print(rot)
        publish_transforms(br,trans,rot,trans1,rot1)
        rate.sleep()

        print('here the transform from world frame to target frame')
        print(trans1)
        print(rot1)
        publish_transforms(br,trans,rot,trans1,rot1)
        rate.sleep()
