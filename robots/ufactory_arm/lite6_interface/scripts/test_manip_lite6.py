#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import math

from lite6_interface.lite6_interface import Lite6Interface


def main():
    rospy.init_node("test_manip_lite6", anonymous=True)
    ri = Lite6Interface("lite6")

    # Initial Pose
    rospy.loginfo("Moving to Initial Pose")
    ri.fk([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Pose 1
    rospy.loginfo("Moving to Pose 1")
    ri.fk([40.0, 30.0, 20.0, 10.0, 0.0, 0.0])

    # Pose 2
    rospy.loginfo("Moving to Pose 2")
    ri.ik_relative([0.0, 0.0, -0.05, 0.0, 0.0, 0.0])

    # Pose 3
    rospy.loginfo("Moving to Pose 3")
    ri.fk([-40.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Pose 4
    rospy.loginfo("Moving to Pose 4")
    ri.ik_relative([0.05, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Back to Initial Pose
    rospy.loginfo("Moving to Initial Pose again")
    ri.fk([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])


    rospy.loginfo("End")


if __name__ == '__main__':
    main()
