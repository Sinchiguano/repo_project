#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function, division

import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

g_world_frame = '/world'
g_camera_frame = '/camera_link'
g_tcp_frame = '/yumi_tcp'

rospy.init_node('tf_listener_on_input')

listener = tf.TransformListener()

rate = rospy.Rate(10.0)
with open('pointlist.txt', 'w') as f:
    while not rospy.is_shutdown():
        raw_input('Press enter')
        time = rospy.Time.now() - rospy.Duration(0.2)
        try:
            # somehow working (trans1, rot1) = listener.lookupTransform(g_tcp_frame, g_world_frame, time)
            (trans1, rot1) = listener.lookupTransform(g_world_frame, g_tcp_frame, time)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            print(e)
            continue
        try:
            (trans2, rot2) = listener.lookupTransform(g_world_frame, g_camera_frame, time)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            print(e)
            continue

        f.write('{0[0]}, {0[1]}, {0[2]}, {1[0]}, {1[1]}, {1[2]}\n'.format(trans1, trans2))
        rate.sleep()
