#!/usr/bin/env python

import math
import rospy, geometry_msgs.msg
from moveit_commander import MoveGroupCommander, RobotCommander
from geometry_msgs.msg import Pose, PoseStamped


def deg2rad(deg):
    return math.radians(deg)


def rad2deg(rad):
    return math.degrees(rad)


class RobotInterface(object):
    def __init__(self, move_group_name):
        self.group = MoveGroupCommander(move_group_name)
        self.group.set_planning_time(600.0)

        # Getting Initial Pose & RPY
        self.pose_init = self.group.get_current_pose()
        self.pose_current = self.pose_init
        self.rpy_init  = self.group.get_current_rpy()
        self.rpy_current = self.rpy_init
        self.angle_current = self.group.get_current_joint_values()
        rospy.loginfo("Get Initial Pose\n{}".format(self.pose_init))
        rospy.loginfo("Get Initial RPY:{}".format(self.rpy_init))

        self.target_angle = []
        self.pose_target = []


    def update_current_pose(self):
        self.pose_current = self.group.get_current_pose()
        rospy.loginfo("Get Current Pose:\n{}\n".format(self.pose_current))


    def update_current_rpy(self):
        self.rpy_current = self.group.get_current_rpy()
        rospy.loginfo("Get Current RPY:\n{}\n".format(self.rpy_current))


    def ik(self, pose_target):
        '''
        arg:
        - pose_target: [x, y, z, R, P, Y] [m(xyz), rad(RPY)]
        -- target position values in absolute coordinates
        '''
        self.pose_target = pose_target
        self.group.set_pose_target(self.pose_target)
        self.move()


    def ik_relative(self, pose_diff):
        '''
        arg:
        - pose_target: [x, y, z, R, P, Y] [m(xyz), deg(RPY)]
        -- relative values from current pose
        '''
        # calculate target pose
        self.update_current_pose()
        self.update_current_rpy()
        x_current = self.pose_current.pose.position.x
        y_current = self.pose_current.pose.position.y
        z_current = self.pose_current.pose.position.z
        x_diff = pose_diff[0]
        y_diff = pose_diff[1]
        z_diff = pose_diff[2]
        r_rot_current = self.rpy_current[0]
        p_rot_current = self.rpy_current[1]
        y_rot_current = self.rpy_current[2]
        r_rot_diff = deg2rad(pose_diff[3])
        p_rot_diff = deg2rad(pose_diff[4])
        y_rot_diff = deg2rad(pose_diff[5])
        self.pose_target = [x_current+x_diff, y_current+y_diff, z_current+z_diff, r_rot_current+r_rot_diff, p_rot_current+p_rot_diff, y_rot_current+y_rot_diff]
        rospy.loginfo('pose_target: {}'.format(self.pose_target))

        # moveit
        self.group.set_pose_target(self.pose_target)
        self.move()


    def fk(self, target_angle_deg):
        '''
        arg:
        - target_angle: [j0, j1, j2, ...] [deg]
        -- target angle values in absolute coordinates
        '''
        self.target_angle = []
        for i in range(len(target_angle_deg)):
            angle = deg2rad(target_angle_deg[i])
            self.target_angle.append(angle)

        rospy.loginfo('target_angle[deg]: {}'.format(target_angle_deg))

        # moveit
        self.group.set_joint_value_target(self.target_angle)
        self.move()


    def fk_relative(self, diff_angle):
        '''
        arg:
        - diff_angle: [j0, j1, j2, ...] [deg]
        -- relative angle values from current joint values
        '''
        # calculate target angle
        self.angle_current = self.group.get_current_joint_values()
        self.target_angle = []
        target_angle_deg = []
        for i in range(len(self.angle_current)):
            angle = self.angle_current[i] + deg2rad(diff_angle[i])
            angle_deg = deg2rad(angle)
            self.target_angle.append(angle)
            target_angle_deg.append(angle_deg)

        rospy.loginfo('target_angle[deg]: {}'.format(target_angle_deg))

        # moveit
        self.group.set_joint_value_target(self.target_angle)
        self.move()


    def reset_pose(self):
        self.group.set_joint_value_target([0.0, -0.3, 0.0, math.pi/2.0])
        self.move()


    def move_sim_robot(self):
        self.group.go()
        rospy.sleep(0.1)  # need to change to interpolation time

        self.angle_current = self.group.get_current_joint_values()
        angle_current_deg = []
        for i in range(len(self.angle_current)):
            angle_deg = rad2deg(self.angle_current[i])
            angle_current_deg.append(angle_deg)

        self.target_angle = self.angle_current  # update target_angle for commands which move joints directly

        rospy.loginfo('angle_current[deg]: {}'.format(angle_current_deg))


    def move_real_robot(self):
        'This is assumed to be overriden by each robot interface'
        print('')


    def move(self):
        self.move_sim_robot()
        self.move_real_robot()
