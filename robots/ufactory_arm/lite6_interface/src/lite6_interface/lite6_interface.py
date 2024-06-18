#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

from robot_interface import RobotInterface


class Lite6Interface(RobotInterface):
    def __init__(self, robot_name='Lite6'):
        print('init')
        super().__init__(robot_name)

    #def move(self):
    #    move;
