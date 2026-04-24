#!/usr/bin/env python3

import rospy
from robot_model import RobotModel

class PandaRobotModel(RobotModel):
    def __init__(self,
                 name = ["panda_finger_joint1", "panda_finger_joint2", "panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7"],
                 position = [0, 0, 0, 0, 0, 0, 0, 0, 0.785], # 0.785 = pi/4
                 velocity = [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 effort = [0, 0, 0, 0, 0, 0, 0, 0, 0]):
        print("init PandaRobotModel")

        super(PandaRobotModel, self).__init__(name, position, velocity, effort)



if __name__ == '__main__':
    panda = PandaRobotModel()

    while not rospy.is_shutdown():
        panda.joint_state.header.stamp = rospy.Time.now()
        panda.pub.publish(panda.joint_state)
        panda.rate.sleep()


