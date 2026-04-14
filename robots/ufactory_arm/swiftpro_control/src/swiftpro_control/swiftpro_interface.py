#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import sys

from robot_interface.robot_interface import RobotInterface,deg2rad,rad2deg

PYTHON_VER = sys.version_info.major


class SwiftproInterface(RobotInterface):
    def __init__(self, move_group_name='arm'):
        if PYTHON_VER == 3:
            super().__init__(move_group_name)
        else:
            super(SwiftproInterface, self).__init__(move_group_name)

        self.move_group_name = move_group_name

    #def move(self):
    #    move;
