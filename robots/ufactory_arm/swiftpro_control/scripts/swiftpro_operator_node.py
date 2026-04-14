#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from swiftpro_control.swiftpro_operator import SwiftproOperator


def main():
    rospy.init_node('swiftpro_operator_node', anonymous=True)

    # Generate instance
    sp_operator = SwiftproOperator()
    sp_operator.standby_pose()

    # Run
    rospy.spin()


if __name__ == '__main__':
    main()
