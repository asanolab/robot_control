#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

class RobotModel(object):
    def __init__(self, name, position, velocity, effort):
        print("init RobotModel")
        rospy.init_node('robot_model_node', anonymous=True)

        self.pub = rospy.Publisher('joint_states', JointState, queue_size=1)
        self.sub = rospy.Subscriber('send_joint_states', JointState, self.callback)
        self.rate = rospy.Rate(10)

        self.joint_state = JointState()
        self.joint_state.header = Header()
        self.joint_state.header.stamp = rospy.Time.now()
        self.joint_state.name = name
        self.joint_state.position = position
        self.joint_state.velocity = velocity
        self.joint_state.effort = effort

    def callback(self, data):
        for i in range(len(data.position)):
            self.joint_state.position[i] = data.position[i]

