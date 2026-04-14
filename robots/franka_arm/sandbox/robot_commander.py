#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

class RobotCommander(object):
    def __init__(self, name, position, velocity, effort):
        print("init RobotCommander")
        rospy.init_node('robot_commander_node')

        self.pub = rospy.Publisher('send_joint_states', JointState, queue_size=1)
        self.rate = rospy.Rate(10)

        self.joint_state = JointState()
        self.joint_state.header = Header()
        self.joint_state.header.stamp = rospy.Time.now()
        self.joint_state.name = name
        self.joint_state.position = position
        self.joint_state.velocity = velocity
        self.joint_state.effort = effort


    def send(self, data):
        self.joint_state.header.stamp = rospy.Time.now()

        for i in range(len(data)):
            self.joint_state.position[i] = data[i]

        print(self.joint_state.position)
        self.pub.publish(self.joint_state)


