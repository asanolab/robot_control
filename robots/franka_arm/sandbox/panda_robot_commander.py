#!/usr/bin/env python

from robot_commander import RobotCommander

class PandaRobotCommander(RobotCommander):
    def __init__(self,
                 name = ["panda_finger_joint1", "panda_finger_joint2", "panda_joint1", "panda_joint2", "panda_joint3", "panda_joint4", "panda_joint5", "panda_joint6", "panda_joint7"],
                 position = [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 velocity = [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 effort = [0, 0, 0, 0, 0, 0, 0, 0, 0]):
        print("init PandaRobotCommander")

        super(PandaRobotCommander, self).__init__(name, position, velocity, effort)


print("exceute below:")
print("prc = PandaRobotCommander()")
print("prc.send([0, 0, 20, 20, 20, 20, 20, 20, 20])")
