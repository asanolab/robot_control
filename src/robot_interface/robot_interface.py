#!/usr/bin/env python

import math
import rospy, geometry_msgs.msg
from moveit_commander import MoveGroupCommander, RobotCommander
from geometry_msgs.msg import Pose, PoseStamped


class RobotInterface():
    def __init__(self, robot_name):
        rospy.init_node("moveit_command_sender")
        self.group = MoveGroupCommander(robot_name)
        self.group.set_planning_time(600.0)

        # Getting Initial Pose & RPY
        self.pose_init = self.group.get_current_pose()
        self.rpy_init  = self.group.get_current_rpy()
        rospy.loginfo("Get Initial Pose\n{}".format(self.pose_init))
        rospy.loginfo("Get Initial RPY:{}".format(self.rpy_init))

    def get_current_pose(self):
        pose_current = self.group.get_current_pose()
        rospy.loginfo("Get Current Pose:\n{}\n".format(pose_current))

    def ik(self, pose_target):
        self.group.set_pose_target(pose_target)
        self.group.go()
        rospy.sleep(0.5)
        rospy.loginfo('angle_vector: {}'.format(self.group.get_current_joint_values()))

    def fk(self, pose_target):
        self.group.set_joint_value_target(pose_target)
        self.group.go()
        rospy.sleep(0.5)
        rospy.loginfo('angle_vector: {}'.format(self.group.get_current_joint_values()))

    def reset_pose(self):
        self.group.set_joint_value_target([0.0, -0.3, 0.0, math.pi/2.0])
        self.group.go()
        rospy.sleep(0.5)
        rospy.loginfo('angle_vector: {}'.format(self.group.get_current_joint_values()))
