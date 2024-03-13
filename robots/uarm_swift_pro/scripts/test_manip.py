#!/usr/bin/env python

import rospy
import math

from robot_interface import RobotInterface


def main():
    rospy.init_node("test_manip", anonymous=True)
    ri = RobotInterface("arm")

    # Pose 1
    rospy.loginfo("Starting Pose 1")
    ri.ik([0.12, 0.0, 0.1, 0.0, math.pi/2.0, 0.0])

    # Pose 2
    rospy.loginfo("Starting Pose 2")
    ri.ik([0.2, 0.0, 0.2, 0.0, 0.0, 0.0])

    # Pose 3
    rospy.loginfo("Starting Pose 3")
    ri.fk([0.5, 0.0, 0.0, 0.0])

    # Pose 4
    rospy.loginfo("Starting Pose 4")
    ri.fk([0.5, 0.0, -0.5, 0.0])

    # Back to Initial Pose
    rospy.loginfo("Back to Initial Pose")
    ri.reset_pose()

    rospy.loginfo("End")


if __name__ == '__main__':
    main()
