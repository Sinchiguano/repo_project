#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.


import sys
sys.path.insert(0, '/home/casch/yumi_depends_ws/src/thesis_pkg/yumi_main/scripts/project')
from thesis_library import *


##convert a rot and trans matrix to a 4x4 matrix
def data_to_transform(r_matrix,t_position):
    mat =np.hstack((r_matrix,t_position))
    mat=np.vstack((mat,[0.0,0.0,0.0,1.0]))
    return mat

#convert a 4x4 matrix to a Pose message
def transform_to_pose(mat):
    pose = Pose()
    pose.position.x = mat[0,3]
    pose.position.y = mat[1,3]
    pose.position.z = mat[2,3]
    quat = tf.transformations.quaternion_from_matrix(mat)
    pose.orientation.x = quat[0]
    pose.orientation.y = quat[1]
    pose.orientation.z = quat[2]
    pose.orientation.w = quat[3]
    return pose

def publish_transforms(br, pose):


    # t0 = geometry_msgs.msg.TransformStamped()
    # t0.header.stamp = rospy.Time.now()
    # t0.header.frame_id = "world"
    # t0.child_frame_id = "panda_link0"
    # t0.transform.translation.x = 0.0
    # t0.transform.translation.y = 0.0
    # t0.transform.translation.z = 0.0

    # tmp_rot=np.array([[1,0, 0], [0, 1, 0],[0, 0, 1]])
    # tmp_trans=np.array([[0.30],[0],[0] ])
    # myrot =np.hstack((tmp_rot,tmp_trans))
    # myrot=np.vstack((myrot,[0.0,0.0,0.0,1.0]))

    # q0 = tf.transformations.quaternion_from_matrix(myrot)
    # t0.transform.rotation.x = q0[0]
    # t0.transform.rotation.y = q0[1]
    # t0.transform.rotation.z = q0[2]
    # t0.transform.rotation.w = q0[3]
    # br.sendTransform(t0)



    t2 = geometry_msgs.msg.TransformStamped()
    t2.header.stamp = rospy.Time.now()
    t2.header.frame_id = "yumi_tcp"#"world"#
    t2.child_frame_id = "camera_link"
    t2.transform.translation = pose.position
    t2.transform.rotation = pose.orientation
    br.sendTransform(t2)

def print_information(rotation_vector,translation_vector,rvec_matrix):

    print("\n\nThe world coordinate systems origin in-->> camera's coordinate system:")
    print("===rotation_vector:")
    print(rotation_vector)
    print("===rotation_matrix:")
    print(rvec_matrix)
    print("===translation_vector:")
    print(translation_vector)

    print("\n\nThe camera origin in -->>world coordinate system:")
    print("===camera rvec_matrix:")
    print(rvec_matrix.T)
    print("===camera translation_vector:")
    print(-np.dot(rvec_matrix.T, translation_vector))

def draw_show_on_image(frame,axi_imgpts,corners,ret,line_width=2):


    # cv2.drawChessboardCorners(frame, (8,9), corners, ret)
    cv2.line(frame, tuple(axi_imgpts[3].ravel()), tuple(axi_imgpts[1].ravel()), (0,255,0), line_width) #GREEN Y
    cv2.line(frame, tuple(axi_imgpts[3][0]), tuple(axi_imgpts[2].ravel()), (255,0,0), line_width) #BLUE Z
    cv2.line(frame, tuple(axi_imgpts[3,0]), tuple(axi_imgpts[0].ravel()), (0,0,255), line_width) #RED x

    text_pos = (axi_imgpts[0].ravel() + np.array([3.5,-7])).astype(int)
    cv2.putText(frame,'X', tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))
    text_pos = (axi_imgpts[1].ravel() + np.array([3.5,-7])).astype(int)
    cv2.putText(frame,'Y', tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))
    text_pos = (axi_imgpts[2].ravel() + np.array([3.5,-7])).astype(int)
    cv2.putText(frame,'Z', tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))

    text_pos = (axi_imgpts[3].ravel() + np.array([200,50])).astype(int)
    cv2.putText(frame,'1unit=1cm', tuple(text_pos),cv2.FONT_HERSHEY_PLAIN, 1, (0, 0,255))

    # Display the resulting frame
    cv2.imshow('Target locator',frame)
    cv2.imwrite('test.jpg', frame)

def locate_target_orientation(frame,ret, corners):

    # 3D world points.
    x,y=np.meshgrid(range(8),range(9))#col row vertical
    world_points_3d=np.hstack((y.reshape(72,1)*0.01,x.reshape(72,1)*0.01,np.zeros((72,1)))).astype(np.float32)

    # Camera internals
    #Intrinsic parameters===>>> from the intrinsic calibration!!!!
    list_matrix=[616.5322265625, 0, 323.4304504394531, 0, 616.58984375, 233.87391662597656, 0, 0, 1]
    cameraMatrix_ar=np.asarray(list_matrix).reshape(3,3)

    distCoef=[0.1852661379687586, -0.264551739977949, -0.03684812841833995, 0.0009882520270208214, 0]
    distCoef_ar=np.asarray(distCoef).reshape(len(distCoef),1)

    #Rotation vector (radians)
    (success, rotation_vector, translation_vector) = cv2.solvePnP(world_points_3d, corners, cameraMatrix_ar, distCoef_ar, flags=cv2.SOLVEPNP_ITERATIVE)

    # World coordinates system
    axis = np.float32([[0.09,0,0],[0,0.08,0],[0,0,0.06],[0,0,0]])
    axis_imgpts, jacobian = cv2.projectPoints(axis, rotation_vector, translation_vector,cameraMatrix_ar, distCoef_ar)

    # Rotation_vector into rotation_matrix
    rvec_matrix = cv2.Rodrigues(rotation_vector)[0]


    return axis_imgpts,corners,ret,rvec_matrix,translation_vector,rotation_vector

def main():

    br = tf2_ros.TransformBroadcaster()

    rate = rospy.Rate(10)
    counter=0
    while not rospy.is_shutdown():

        counter+=1

        # Capture frame-by-frame
        #frame=cv2.imread('temp3.jpg')
        frame=camObj.get_image()

        if frame is None:
            print('no image!!!')
            continue

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('temp3.jpg', frame)
            break
        try:
            # 2D image points
            ret, corners = cv2.findChessboardCorners(frame, (8,9))

            corners=corners.reshape(-1,2)#undefied number of rows
            if not ret:
                print('\nPlease, locate well the calibration target!!!')
                continue
        except Exception as ex:
            print('\nStatus of findChessboardCorners: {}'.format(ret))
            print('Please, locate well the calibration target!!!')
            print(ex)
            print('-------------------------------------------------')
            continue

        # Extrinsic calibration!!!
        axis_imgpts,corners,ret,rvec_matrix,translation_vector,rotation_vector= locate_target_orientation(frame,ret, corners)

        # print information about rotation and translation for the camera and world frame
        print_information(rotation_vector,translation_vector,rvec_matrix)

        #draw and display lines and text on the image
        draw_show_on_image(frame,axis_imgpts,corners,ret)


        # get transform matrix from rotation and translation of the camera frame relative to the world frame
        mat=data_to_transform(rvec_matrix.T,-np.dot(rvec_matrix.T, translation_vector))
        
         # get the pose of the camera frame relative to the world frame
        pose=transform_to_pose(mat)

        # publish transform of the camera frame
        publish_transforms(br, pose)

        # we should expect to go through the loop 10 times per second
        rate.sleep()

        print('\ncounter:',counter,'\n')

    # When everything done, release the capture
    cv2.destroyAllWindows()


if __name__ == '__main__':
    camObj=camera()
    main()
