#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

from robot_interface.robot_interface import RobotInterface


class SwiftproInterface(RobotInterface):
    def __init__(self, robot_name='Swiftpro'):
        print('init')
        super().__init__(robot_name)

    #def move(self):
    #    move;
