#!/usr/bin/env python

import rospy
from swiftpro.msg import status


def main():
    rospy.init_node("pump_on")

    pub = rospy.Publisher("pump_topic", status, queue_size=1)
    rate = rospy.Rate(10)
    msg = status(status=0)  # 0: pump off, 1: pump on

    for i in range(10):
        pub.publish(msg)
        rospy.loginfo("published")
        rate.sleep()


if __name__ == '__main__':
    main()
