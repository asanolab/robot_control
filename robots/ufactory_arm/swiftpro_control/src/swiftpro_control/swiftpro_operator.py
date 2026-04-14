#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import rospy
import time
from std_msgs.msg import Bool

from swiftpro_control.swiftpro_interface import SwiftproInterface
from swiftpro.msg import status


# swift pro operation via ROS msg
class SwiftproOperator(object):
    def __init__(self):
        # robot interface
        self.ri = SwiftproInterface('arm')  # arg: move group name

        # publisher
        self.pub_complete = rospy.Publisher('/swiftpro_operator/complete_suction', Bool, queue_size=1)

        # subscriber
        rospy.Subscriber('/swiftpro_operator/start_suction', Bool, self.start_suction_cb, queue_size=1)
        rospy.Subscriber('/swiftpro_operator/stop_suction',  Bool, self.stop_suction_cb, queue_size=1)
        rospy.Subscriber('/complete_handover',               Bool, self.standby_pose_cb, queue_size=1)

        time.sleep(0.5)  # wait for pub/sub register
        time.sleep(2)    # wait for initial pose


    # callback
    def start_suction_cb(self, msg):
        if msg.data:
            self.start_suction()


    def stop_suction_cb(self, msg):
        if msg.data:
            self.stop_suction()


    def standby_pose_cb(self, msg):
        if msg.data:
            self.standby_pose()


    # functions
    def standby_pose(self):
        rospy.loginfo("Standby pose before suction")
        self.ri.fk([-90.0, 0.0, 60.0, 0.0])  # joint2:65 is NG


    def handover_pose(self):
        rospy.loginfo("Handover pose")
        self.ri.fk([0.0, 0.0, 0.0, 0.0])


    def start_suction(self):
        pub = rospy.Publisher("pump_topic", status, queue_size=1)
        rate = rospy.Rate(10)
        msg = status(status=1)  # 0: pump off, 1: pump on

        # pick-up motion
        rospy.loginfo("Pick-up pose")
        self.ri.fk([-40.0, 0.0, 0.0, 0.0])  # rotate end-effector upright on the plate
        self.ri.fk([-40.0, 33.0, 26.0, 0.0]) # down
        #self.ri.ik_relative([0.0, 0.0, -0.16, 0.0, 0.0, 0.0])  # down

        # pump on
        for i in range(10):
            pub.publish(msg)
            rospy.loginfo("Pump start")
            rate.sleep()

        self.ri.fk([-40.0, 0.0, 0.0, 0.0])  # pick-up
        #self.ri.ik_relative([0.0, 0.0, 0.08, 0.0, 0.0, 0.0])  # pick-up

        # move to handover pose
        self.handover_pose()

        # publish completion
        self.pub_complete.publish(Bool(data=True))

        rospy.loginfo("End of suction")


    def stop_suction(self):
        rospy.loginfo('Stop suction')

        pub = rospy.Publisher("pump_topic", status, queue_size=1)
        rate = rospy.Rate(10)
        msg = status(status=0)  # 0: pump off, 1: pump on

        for i in range(10):
            pub.publish(msg)
            rospy.loginfo("published")
            rate.sleep()
