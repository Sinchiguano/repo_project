#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Take a list of points as input with lines in format:
#  (local_x, local_y, local_z, global_x, global_y, global_z).
# Also optionally taakes the sticker id as input.
# Returns the pose of the sticker.
#
# The algorithm for the spatial version is based on Besl, P. J. & McKay, N. D.,
# "A method for registration of 3-D shapes", IEEE Transactions on Pattern
# Analysis and Machine Intelligence, 1992, 14, 239-256.
# The algorithm for the planar version is based on F. Lu and E. Milios, "Robot
# Pose Estimation in Unknown Environments by Matching 2D Range Scans", Journal
# of Intelligent & Robotic Systems, 1997.
# The closed-form equations for the computation of the transform between 2D
# point clouds give a local optimum.
#
# Test data generation:
# Planar case:
# >>> import numpy as np
# >>> from get_sticker_pose_from_pointlist import get_sticker_pose_pointlist_3d
#
# >>> # Noise-free data
# >>> yaw = 1.3
# >>> tx = 0.5
# >>> ty = -0.8
# >>> transf = np.array([[np.cos(yaw), -np.sin(yaw), tx],
# >>>                    [np.sin(yaw), np.cos(yaw), ty],
# >>>                    [0, 0, 1]])
# >>> local = np.array([
# >>>     [0, 0, 1],
# >>>     [-0.05, 0.05, 1]]).transpose()
# >>> global_ground_truth = transf @ local
# >>> for l, g in zip(local.transpose(), global_ground_truth.transpose()):
# >>>     print('{},{},0,{},{},0'.format(l[0], l[1], g[0], g[1]))
# >>>
# >>> # Data with noise
# >>> noise_xy = 0.05
# >>> local = 10 * np.random.rand(3, 10)
# >>> local[2, :] = 1
# >>> global_ground_truth = transf @ local
# >>> global_measured = global_ground_truth + np.random.randn(3, 10) * noise_xy
# >>> global_measured[2, :] = 1
# >>> for l, g in zip(local.transpose(), global_measured.transpose()):
# >>>     print('{},{},0,{},{},0'.format(l[0], l[1], g[0], g[1]))
#
# Space case:
# >>> import numpy as np
# >>> from get_sticker_pose_from_pointlist import get_sticker_pose_pointlist_6d
# >>> from get_sticker_pose_from_pointlist import matrix_from_quaternion
# >>>
# >>> # 'gt_' prefix = ground-truth.
# >>> # 'h_' prefix = homogeneous.
# >>> # 'm_' prefix = homogeneous.
# >>>
# >>> def to_homogeneous(x):
# >>>     h_x = np.ones((4, len(x)))
# >>>     h_x[:3,:] = x.transpose()
# >>>     return h_x
# >>>
# >>> def from_homogeneous(h_x):
# >>>     return h_x[:3, :].transpose()
# >>>
# >>> def random_quaternion():
# >>>     """Generate a random rotation
# >>>     """
# >>>     a, b, c = np.random.rand(3)
# >>>     q = np.array([np.sqrt(1 - a) * np.sin(2 * np.pi * b),
# >>>                   np.sqrt(1 - a) * np.cos(2 * np.pi * b),
# >>>                   np.sqrt(a) * np.sin(2 * np.pi * c),
# >>>                   np.sqrt(a) * np.cos(2 * np.pi * c)])
# >>>     if q[0] < 0:
# >>>         q = -q
# >>>     return q / np.linalg.norm(q)
# >>>
# >>>
# >>>
# >>> # Noise-free data.
# >>> q = random_quaternion()
# >>> tx = 0.5
# >>> ty = -0.8
# >>> tz = -1.2
# >>> h_gt_transf = np.identity(4)
# >>> h_gt_transf[:3, 3] = (tx, ty, tz)
# >>> h_gt_transf[:3, :3] = matrix_from_quaternion(q)
# >>> local = np.random.rand(5, 3)
# >>> h_local = to_homogeneous(local)
# >>> h_gt_global = h_gt_transf @ h_local
# >>> gt_global = from_homogeneous(h_gt_global)
# >>> dx, dy, dz, qx, qy, qz, qw, err = get_sticker_pose_pointlist_6d(local, gt_global)
# >>> h_transf = np.identity(4)
# >>> h_transf[:3, 3] = (dx, dy, dz)
# >>> h_transf[:3, :3] = matrix_from_quaternion((qw, qx, qy, qz))
# >>> h_global_ = h_transf @ h_local
# >>> global_ = from_homogeneous(h_global_)
# >>> print('Noise-free data')
# >>> print('original transform: {0}, {1}, {2}, {3[0]}, {3[1]}, {3[2]}, {3[3]}'.format(
# >>>     tx, ty, tz, q))
# >>> print('obtained transform: {}, {}, {}, {}, {}, {}, {}'.format(
# >>>     dx, dy, dz, qw, qx, qy, qz))
# >>> print('ground_truth --> obtained: error')
# >>> for l, g, e in zip(gt_global, global_, err):
# >>>     print('{0[0]},{0[1]},{0[2]} --> {1[0]},{1[1]},{1[2]}: {2}'.format(l, g, e))
# >>>
# >>> # Data with noise
# >>> noise_xyz = 0.05
# >>> local = np.random.rand(20, 3)
# >>> h_local = to_homogeneous(local)
# >>> h_gt_global = h_gt_transf @ h_local
# >>> gt_global = from_homogeneous(h_gt_global)
# >>> m_global = gt_global + noise_xyz * np.random.rand(*gt_global.shape)
# >>> dx, dy, dz, qx, qy, qz, qw, err = get_sticker_pose_pointlist_6d(local, m_global)
# >>> h_transf = np.identity(4)
# >>> h_transf[:3, 3] = (dx, dy, dz)
# >>> h_transf[:3, :3] = matrix_from_quaternion((qw, qx, qy, qz))
# >>> h_global_ = h_transf @ h_local
# >>> global_ = from_homogeneous(h_global_)
# >>> print('\nData with noise {}'.format(noise_xyz))
# >>> print('original transform: {0}, {1}, {2}, {3[0]}, {3[1]}, {3[2]}, {3[3]}'.format(
# >>>     tx, ty, tz, q))
# >>> print('obtained transform: {}, {}, {}, {}, {}, {}, {}'.format(
# >>>     dx, dy, dz, qw, qx, qy, qz))
# >>> print('ground_truth --> obtained: error')
# >>> for l, g, e in zip(m_global, global_, err):
# >>>     print('{0[0]},{0[1]},{0[2]} --> {1[0]},{1[1]},{1[2]}: {2}'.format(l, g, e))
from __future__ import print_function

import sys

import numpy as np


def matrix_from_quaternion(q):
    """Rotation matrix from unit-quaternion

    The quaternion has the form q[0] + i * q[1] + j * q[2] + k * q[3], with
    q[0] >= 0 and (q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2) = 1.
    """
    return np.array([
        [1 -  2 * q[2] ** 2 -  2 * q[3] ** 2,
         2 * (q[1] * q[2] - q[0] * q[3]),
         2 * (q[1] * q[3] + q[0] * q[2])],
        [2 * (q[1] * q[2] + q[0] * q[3]),
         1 - 2 * q[1] ** 2 - 2 * q[3] ** 2,
         2 * (q[2] * q[3] - q[0] * q[1])],
        [2 * (q[1] * q[3] - q[0] * q[2]),
         2 * (q[2] * q[3] + q[0] * q[1]),
         1 - 2 * q[1] ** 2 - 2 * q[2] ** 2]])


def euler_from_matrix(matrix):
    """Return Euler angles from rotation matrix

    From transfomations.py in ROS package ros-melodic-tf with without the axes
    specification, set to 'sxyz'.

    Untested!
    """
    # epsilon for testing whether a number is close to zero
    _EPS = np.finfo(float).eps * 4.0

    i = 0
    j = 1
    k = 2

    M = np.array(matrix, dtype=np.float64, copy=False)[:3, :3]
    cy = np.sqrt(M[i, i]*M[i, i] + M[j, i]*M[j, i])
    if cy > _EPS:
        ax = np.arctan2( M[k, j],  M[k, k])
        ay = np.arctan2(-M[k, i],  cy)
        az = np.arctan2( M[j, i],  M[i, i])
    else:
        ax = np.arctan2(-M[j, k],  M[j, j])
        ay = np.arctan2(-M[k, i],  cy)
        az = 0.0

    return ax, ay, az


def euler_from_quaternion(quaternion):
    """Return Euler angles from quaternion
    """
    return euler_from_matrix(matrix_from_quaternion(quaternion))


def get_sticker_pose_pointlist(pointlist_file):
    """
    Each line of pointlist_file must have the format
    (local_x, local_y, local_z, global_x, global_y, global_z)
    """
    pointlist = np.loadtxt(pointlist_file, delimiter=',')
    local_points = pointlist[:, :3]
    global_points = pointlist[:, 3:]
    lmean = local_points.mean(axis=0)
    gmean = global_points.mean(axis=0)
    if (np.any(local_points[:, 2] - lmean[2] != 0)
        or np.any(global_points[:, 2] - gmean[2] != 0)):
        dx, dy, dz, qx, qy, qz, qw, error = get_sticker_pose_pointlist_6d(
            local_points, global_points)
        r, p, y = euler_from_quaternion((qx, qy, qz, qw))
        print('Euler angles untested, use quaternions ' +
              '(x, y, z, w) = ({}, {}, {}, {}) instead'.format(
                  qx, qy, qz, qw), file=sys.stderr)
        return dx, dy, dz, r, p, y, error
    else:
        dx, dy, yaw, error = get_sticker_pose_pointlist_3d(
            local_points, global_points)
        return dx, dy, 0, 0, 0, yaw, error


def get_sticker_pose_pointlist_3d(local_points, global_points):
    """Return the transform from co-planar points

    Return (dx, dy, yaw, error).
    """
    lmean = local_points.mean(axis=0)
    gmean = global_points.mean(axis=0)
    if (np.any(local_points[:, 2] - lmean[2] != 0)
        or np.any(global_points[:, 2] - gmean[2] != 0)):
        raise ValueError('All z-coord. must be equal')
    ldx = local_points[:, 0] - lmean[0]
    ldy = local_points[:, 1] - lmean[1]
    gdx = global_points[:, 0] - gmean[0]
    gdy = global_points[:, 1] - gmean[1]
    s_ldx_gdy = (ldx * gdy).sum()
    s_ldy_gdx = (ldy * gdx).sum()
    s_ldx_gdx = (ldx * gdx).sum()
    s_ldy_gdy = (ldy * gdy).sum()
    yaw = np.arctan2(s_ldx_gdy - s_ldy_gdx, s_ldx_gdx + s_ldy_gdy)
    c_ = np.cos(yaw)
    s_ = np.sin(yaw)
    trans_x = gmean[0] - (lmean[0] * c_ - lmean[1] * s_)
    trans_y = gmean[1] - (lmean[0] * s_ + lmean[1] * c_)
    transformed_x = local_points[:, 0] * c_ - local_points[:, 1] * s_ + trans_x
    transformed_y = local_points[:, 0] * s_ + local_points[:, 1] * c_ + trans_y
    error = np.sqrt((transformed_x - global_points[:,0]) ** 2 +
                    (transformed_y - global_points[:,1]) ** 2)
    return trans_x, trans_y, yaw, error


def get_sticker_pose_pointlist_6d(local_points, global_points):
    """Return the transform from arbitrary points

    Return (dx, dy, dz, qx, qy, qz, qw, error).
    """
    # Equations number refer to Besl, P. J. & McKay, N. D., "A method for
    # registration of 3-D shapes", IEEE Transactions on Pattern Analysis and
    # Machine Intelligence, 1992, 14, 239-256.
    # The set of measured points, P in the article, are the local points.
    # The set of model points, X in the article, are the global points.

    lmean = local_points.mean(axis=0)
    gmean = global_points.mean(axis=0)
    # cross is the cross-covariance, Eq. (24).
    ldx = local_points[:, 0] - lmean[0]
    ldy = local_points[:, 1] - lmean[1]
    ldz = local_points[:, 2] - lmean[2]
    gdx = global_points[:, 0] - gmean[0]
    gdy = global_points[:, 1] - gmean[1]
    gdz = global_points[:, 2] - gmean[2]
    cross = np.array([
        [(ldx * gdx).mean(), (ldx * gdy).mean(), (ldx * gdz).mean()],
        [(ldy * gdx).mean(), (ldy * gdy).mean(), (ldy * gdz).mean()],
        [(ldz * gdx).mean(), (ldz * gdy).mean(), (ldz * gdz).mean()]])
    # Eq. (25).
    a = cross - cross.transpose()
    delta = np.array([[a[1, 2]], [a[2, 0]], [a[0, 1]]])
    q_24_24 = cross + cross.transpose() - cross.trace() * np.identity(3)
    q = np.zeros((4, 4))
    q[0, 0] = cross.trace()
    q[1:4, 0] = delta.flatten()
    q[0, 1:4] = delta.flatten()
    q[1:4, 1:4] = q_24_24
    # Eigenvalues decomposition.
    w, v = np.linalg.eig(q)
    rotation = v[:, w.argmax()]
    if rotation[0] < 0:
        rotation = -rotation
    # Translation, Eq. (26).
    rotmat = matrix_from_quaternion(rotation)
    translation = gmean[:, np.newaxis] - rotmat @ lmean[:, np.newaxis]
    # Computation of the error.
    transformed_points = (rotmat @ local_points.transpose() + translation).transpose()
    error = np.sqrt(((transformed_points - global_points) ** 2).sum(axis=1))
    return (translation[0, 0], translation[1, 0], translation[2, 0],
            rotation[1], rotation[2], rotation[3], rotation[0],
            error)


if __name__ == '__main__':
    try:
        pointlist_file = sys.argv[1]
    except IndexError:
        print('Usage: {} pointlist_file [id]'.format(sys.argv[0]))
        exit(1)
    try:
        id = sys.argv[2]
    except IndexError:
        id = '?????'

    pose_and_error = get_sticker_pose_pointlist(pointlist_file)
    print('{id} {x} {y} {z} {roll} {pitch} {yaw}'.format(
        id=id,
        x=pose_and_error[0],
        y=pose_and_error[1],
        z=pose_and_error[2],
        roll=pose_and_error[3],
        pitch=pose_and_error[4],
        yaw=pose_and_error[5]))
    print('Transformation error:', file=sys.stderr)
    for i, error in enumerate(pose_and_error[6]):
        print('  Point {}: {}'.format(i + 1, error), file=sys.stderr)
