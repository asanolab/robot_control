#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import math

from swiftpro_interface.swiftpro_interface import SwiftproInterface


def main():
    rospy.init_node("test_manip_swiftpro", anonymous=True)
    ri = SwiftproInterface("arm")

    # Initial Pose
    rospy.loginfo("Moving to Initial Pose")
    ri.fk([0.0, 0.0, 0.0, 0.0])

    # Pose 1
    rospy.loginfo("Moving to Pose 1")
    ri.fk([40.0, 20.0, 10.0, 10.0])

    # Pose 2
    rospy.loginfo("Moving to Pose 2")
    ri.ik_relative([0.0, 0.0, -0.05, 0.0, 0.0, 0.0])

    # Pose 3
    rospy.loginfo("Moving to Pose 3")
    ri.fk([-40.0, 0.0, 0.0, 0.0])

    # Pose 4
    rospy.loginfo("Moving to Pose 4")
    ri.ik_relative([0.0, 0.0, 0.05, 0.0, 0.0, 0.0])

    # Back to Initial Pose
    rospy.loginfo("Moving to Initial Pose again")
    ri.fk([0.0, 0.0, 0.0, 0.0])


    rospy.loginfo("End")


if __name__ == '__main__':
    main()
