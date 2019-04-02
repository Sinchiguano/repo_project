#!/usr/bin/env python
import math
import time

from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import Pose
from std_msgs.msg import Header
import rospy
import tf2_ros
import zmq

import sys
sys.path.insert(0, '/home/casch/yumi_depends_ws/src/thesis_pkg/yumi_main/scripts/project')
from thesis_library import *




def pose_to_tf(x_y_z_qw_qx_qy_qz):
    """input in m and rad"""
    br = tf2_ros.TransformBroadcaster()
    t = TransformStamped()
    #t.header = Header()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'world'
    t.child_frame_id = 'yumi_tcp'
    t.transform.translation.x = x_y_z_qw_qx_qy_qz[0]
    t.transform.translation.y = x_y_z_qw_qx_qy_qz[1]
    t.transform.translation.z = x_y_z_qw_qx_qy_qz[2]
    t.transform.rotation.w = x_y_z_qw_qx_qy_qz[3]
    t.transform.rotation.x = x_y_z_qw_qx_qy_qz[4]
    t.transform.rotation.y = x_y_z_qw_qx_qy_qz[5]
    t.transform.rotation.z = x_y_z_qw_qx_qy_qz[6]
    br.sendTransform(t)


    # pose = Pose()
    # pose.position.x = x_y_z_qw_qx_qy_qz[0]
    # pose.position.y = x_y_z_qw_qx_qy_qz[1]
    # pose.position.z = x_y_z_qw_qx_qy_qz[2]
    # pose.orientation.x = x_y_z_qw_qx_qy_qz[4]
    # pose.orientation.y = x_y_z_qw_qx_qy_qz[5]
    # pose.orientation.z = x_y_z_qw_qx_qy_qz[6]
    # pose.orientation.w = x_y_z_qw_qx_qy_qz[3]
    # return pose


def main():

    #pub_pose = rospy.Publisher('pose_world_yumi_tcp', Pose, queue_size=10)


    context = zmq.Context()

    #  Socket to talk to server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    g_period = 1
    while not rospy.is_shutdown():
        rospy.init_node('tcp_tf', anonymous=True)

        socket.send(b'')

        #  Get the reply.
        message = socket.recv()
        pose_to_tf([float(v) for v in message.split()])
        time.sleep(g_period)



if __name__ == '__main__':
    main()
