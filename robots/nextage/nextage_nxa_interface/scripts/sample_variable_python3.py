#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

MIT License

Copyright (c) 2024 Kawada Robotics Corporation

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import sys

# change import of ANY module depend on python version
if sys.version_info.minor == 8:
    from omniORB import CORBA, any as ANY
elif sys.version_info.minor == 10:
    from omniORB import CORBA
    from NxApiLib import any as ANY

#from omniORB import CORBA
#from NxApiLib import any as ANY

from NxApi import *
#from NxApi_idl import RootNxController

#sys.path.append(os.path.realpath("./idl_NxApi"))
#from NxApi import *


# Set to match the API server startup IP
ipaddr_str = "192.168.0.23"

argv = ["-ORBdefaultWCharCodeSet", "UTF-16", "-ORBgiopMaxMsgSize", "104857600"]
print("hoge")
# Connect to the API server
orb = CORBA.ORB_init(argv, CORBA.ORB_ID)
print("hoge3")
api = orb.string_to_object(
    "corbaloc:iiop:1.2@%s:2809/RootControllerApi" % (ipaddr_str)
)
print("hoge4")
root_controller = api._narrow(RootNxController)
print("hoge5")
# Raising an exception if the maximum number of clients is reached
controller = root_controller.GetNxController("", "")

# Get Controller's variable values
controller_names = [
    "@IF_VERSION",
    "@SYSTEM_VERSION",
    "@AUTO_MODE",
    "@EXT_CONTROL",
    "@SPEED",
    "@DIN",
    "@DOUT",
    "@CS/0",
    "@EMERGENCY_STOP",
    "@EMERGENCY_STOP_CODE",
    "@HOLD_RESTART",
    "@COLLISION_CHECK",
    "@TOTAL_OPERATING_TIME",
]
#print(" ".join(controller_names))
#controller_var = controller.GetVariable(" ".join(controller_names), "")
#controller_values = ANY.from_any(
#    controller_var.Execute("GetValues", ANY.to_any(None))
#)
#for num in range(len(controller_names)):
#    print(controller_names[num] + " : " + str(controller_values[num]))

# Get Robot's variable values
all_robots = controller.GetNxObject("Robot", "All")
robot_names = [
    "@SERVO_ON",
    "@SERVO_STATUS",
    "@JOINT_ANGLE",
    "@BUSY_STATUS",
    "@PAUSE",
    "@PAUSE_CODE",
    "@TOTAL_OPERATING_TIME",
]
robot_var = all_robots.GetVariable(" ".join(robot_names), "")
robot_values = ANY.from_any(robot_var.Execute("GetValues", ANY.to_any(None)))
for num in range(len(robot_names)):
    print(robot_names[num] + " : " + str(robot_values[num]))

rarm = controller.GetNxObject("Robot", "RArm")
rarm_var = rarm.GetVariable("@BASE_POSITION", "")
rarm_values = ANY.from_any(rarm_var.Execute("GetValues", ANY.to_any(None)))
print("@BASE_POSITION(RArm) : " + str(rarm_values[0]))

larm = controller.GetNxObject("Robot", "LArm")
larm_var = larm.GetVariable("@BASE_POSITION", "")
larm_values = ANY.from_any(larm_var.Execute("GetValues", ANY.to_any(None)))
print("@BASE_POSITION(LArm) : " + str(larm_values[0]))

# Get Vision's variable values
vision = controller.GetNxObject("Vision", "")
vision_names = [
    "@INTERNAL_CAMERA_PARAM_RAW/0",
    "@INTERNAL_CAMERA_PARAM/0",
    "@EXTERNAL_CAMERA_PARAM/0",
]
vision_var = vision.GetVariable(" ".join(vision_names), "")
vision_values = ANY.from_any(vision_var.Execute("GetValues", ANY.to_any(None)))
for num in range(len(vision_names)):
    print(vision_names[num] + " : " + str(vision_values[num]))

# Get Task's variable values
task = controller.GetNxObject("Task", "")
task_names = [
    "@STATUS",
    "@PRODUCTION_VOLUME",
    "@PRODUCTION_RECORD",
    "@CYCLE_TIME",
    "@FLOW_DESCRIPTION/1",
    "@FLOW_ERROR_INFO",
]
task_var = task.GetVariable(" ".join(task_names), "")
task_values = ANY.from_any(task_var.Execute("GetValues", ANY.to_any(None)))
for num in range(len(task_names)):
    print(task_names[num] + " : " + str(task_values[num]))


################################# added ####################
# memo
# - authority is needed for write (read is not need)
# - u'' is not necessary in python3 (python2 needs)


# Acquire API Authority
controller.Execute(u"GetAuthority", ANY.to_any(None))


# Get Variable's variable values
task = controller.GetNxObject(u"Task", u"")
print("Task Name: '%s'"%(task.Name))

varlist= ANY.from_any(task.GetVariableNames(u"@GLOBAL_VARS"))
print("varlist: '%s'"%(varlist))

vari1 = task.GetVariable(u"@GLOBAL_VARS/sample1", u"")
vari2 = task.GetVariable(u"@GLOBAL_VARS/sample2", u"")

valu1 = ANY.from_any(vari1.Execute(u"GetValues", ANY.to_any(None)))[0]
valu2 = ANY.from_any(vari2.Execute(u"GetValues", ANY.to_any(None)))[0]
print(valu1)
print(valu2)

count = 1234
label = u"write test"

vari1.Execute(u"SetValues", ANY.to_any([[[u"value", u"%d"%(count)]]]))
vari2.Execute(u"SetValues", ANY.to_any([[[u"value", label]]]))

valu1 = ANY.from_any(vari1.Execute(u"GetValues", ANY.to_any(None)))[0]
valu2 = ANY.from_any(vari2.Execute(u"GetValues", ANY.to_any(None)))[0]
print(valu1)
print(valu2)


# Release API authority
controller.Execute(u"ReleaseAuthority", ANY.to_any(None))
