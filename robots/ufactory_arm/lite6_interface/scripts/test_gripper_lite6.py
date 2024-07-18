#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import math
import time

from lite6_interface.lite6_interface import Lite6Interface


def main():
    rospy.init_node("test_manip_lite6", anonymous=True)
    ri = Lite6Interface("lite6")

    # open
    rospy.loginfo("Open gripper")
    ri.gripper_open()

    print("waiting for 1 second")
    time.sleep(1)

    # close
    rospy.loginfo("Close gripper")
    ri.gripper_close()


if __name__ == '__main__':
    main()
