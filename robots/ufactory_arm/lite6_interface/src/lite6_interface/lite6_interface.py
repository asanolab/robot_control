#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from xarm_msgs.srv import Move,SetInt16

from robot_interface.robot_interface import RobotInterface,deg2rad,rad2deg


class Lite6Interface(RobotInterface):
    def __init__(self, robot_name='lite6'):
        super().__init__(robot_name)
        self.max_speed = 0.35  # [rad/s]
        self.max_acc = 7       # [rad/s^2]
        self.ip_time = 1       # [s]


    def move_real_robot(self):
        rospy.wait_for_service('/ufactory/move_joint')
        try:
            move_joint = rospy.ServiceProxy('/ufactory/move_joint', Move)
            res = move_joint(self.target_angle, self.max_speed, self.max_acc, 0, 0)
            '''
            args (xarm_msgs/srv/Move.srv):
            # pose: target coordinate.
            # mvvelo: (value range: 0 ~ 1000) specified maximum velocity during execution. linear (0 to 1000 mm/s)  or angular (range 0~1000 for 0 to 3.14 rad/s) velocity.
            # mvacc: specified maximum linear acceleration (mm/s^2) during execution. (angular acceleration is fixed currently).
            # mvtime: currently do not have any special meaning, please just give it 0.
            # PLEASE NOTE: after firmware version 1.5, For servo_cartesian motion, mvtime will be used as indicator of coordinate system. (0 for BASE coordinate, non-zero for TOOL coordinate)
            # mvradii: this is special for move_ineb service, meaning the blending radius between 2 straight path trajectories, 0 for no blend.
            '''
            ret = res.ret
            message = res.message

            rospy.sleep(self.ip_time)  # need to change to interpolation time
        except rospy.ServiceException as e:
            print('Service call failed: %s' % e)


    def gripper_command(self, val):
        rospy.wait_for_service('/lite6/vacuum_gripper_set')
        try:
            s = rospy.ServiceProxy('/lite6/vacuum_gripper_set', SetInt16)
            res = s(val)
            rospy.loginfo(res.message)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)


    def gripper_open(self):
        self.gripper_command(1)


    def gripper_close(self):
        self.gripper_command(0)
