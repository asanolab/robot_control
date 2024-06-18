#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

from robot_interface import RobotInterface


class DobotMagicianInterface(RobotInterface):
    def __init__(self, robot_name='DobotMagician'):
        print('init')
        super().__init__(robot_name)

    #def move(self):
    #    move;
