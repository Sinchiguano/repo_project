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


def publish_transforms(trans,rot):

    br = tf2_ros.TransformBroadcaster()

    t10 = geometry_msgs.msg.TransformStamped()
    t10.header.stamp = rospy.Time.now()
    t10.header.frame_id = "world"
    t10.child_frame_id = "camera_link2"
    t10.transform.translation.x = trans[0]
    t10.transform.translation.y = trans[1]
    t10.transform.translation.z = trans[2]

    t10.transform.rotation.x = rot[0]
    t10.transform.rotation.y = rot[1]
    t10.transform.rotation.z = rot[2]
    t10.transform.rotation.w = rot[3]
    br.sendTransform(t10)

if __name__ == '__main__':

    rospy.init_node('cam_tf_listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans1,rot1) = listener.lookupTransform('/world','/camera_link', rospy.Time(0))
            # trans1_mat = tf.transformations.translation_matrix(trans1)
            # rot1_mat   = tf.transformations.quaternion_matrix(rot1)
            # mat1 = numpy.dot(trans1_mat, rot1_mat)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        #
        # try:
        #     (trans1,rot1) = listener.lookupTransform('/camera_link','/yumi_tcp', rospy.Time(0))
        #     trans1_mat = tf.transformations.translation_matrix(trans1)
        #     rot1_mat   = tf.transformations.quaternion_matrix(rot1)
        #     mat2 = numpy.dot(trans1_mat, rot1_mat)
        # except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        #     continue
        #
        # mat3 = numpy.dot(mat1, mat2)
        # trans3 = tf.transformations.translation_from_matrix(mat3)
        # rot3 = tf.transformations.quaternion_from_matrix(mat3)
        # publish_transforms(trans3,rot3)


        print('here the transform from world to camera frame')
        publish_transforms(trans1,rot1)
        print('translation')
        print(trans1)
        print('rotation')
        print(rot1)

        rate.sleep()
