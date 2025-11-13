#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# memo
# - authority is needed for write by changing display line to yellow (read is not need)
# - u'' is not necessary in python3 (python2 needs)

import socket

# NEXTAGE API
from omniORB import CORBA, any as ANY
from NxApi import *


class NextageNXAInterface():
    def __init__(self, ip="192.168.0.10", debug=False):
        self.ipaddr_str = ip
        self.argv = ["-ORBdefaultWCharCodeSet", "UTF-16", "-ORBgiopMaxMsgSize", "104857600"]
        self.task = None
        self.skt = None
        self.port = 5000
        self.debug = debug


    def setup(self, speed=100):
        # Connect to the API server
        self.orb = CORBA.ORB_init(self.argv, CORBA.ORB_ID)
        self.api = self.orb.string_to_object("corbaloc:iiop:1.2@%s:2809/RootControllerApi"%(self.ipaddr_str))

        # Setup controller
        self.root_controller = self.api._narrow(RootNxController)
        self.controller = self.root_controller.GetNxController(u"", u"")
        self.whole_body = self.controller.GetNxObject(u"Robot", u"All")

        # Get Variable's variable values
        self.task = self.controller.GetNxObject(u"Task", u"")
        self.varlist= ANY.from_any(self.task.GetVariableNames(u"@GLOBAL_VARS"))

        # print
        print("Task Name: '%s'"%(self.task.Name))
        if self.debug:
            print("varlist: '%s'"%(self.varlist))

        #speed_var = controller.GetVariable(u"@SPEED", u"")
        #speed = ANY.to_any([["value", speed]])
        #speed_var.Execute(u"SetValues", ANY.to_any([speed]))

        # socket
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skt.connect((self.ipaddr_str, self.port))

        # Get authority
        self.get_authority()

        return


    def set_task(self, target_task_name='task1'):
        if (self.task.Name != target_task_name):
            self.task.Execute(u"SetTask", ANY.to_any([[u"taskName", target_task_name]]))
            print("Task has changed: '%s'"%(self.task.Name))
            pass


    def start_task(self):
        self.task.Execute(u"Start", ANY.to_any([[ "mode", CORBA.Any(CORBA.TC_long,2) ]]))


    # Acquire API Authority
    def get_authority(self):
        self.controller.Execute("GetAuthority", ANY.to_any(None))


    # Release API authority
    def release_authority(self):
        self.controller.Execute("ReleaseAuthority", ANY.to_any(None))


    def servo_on(self):
        self.whole_body.Execute(u"ServoOn", ANY.to_any(None))


    # set/get variables
    def get_var(self, var_name='v_name'):
        s = "@GLOBAL_VARS/" + var_name
        tv_name = self.task.GetVariable(s, "")  # task_var_name
        val = ANY.from_any(tv_name.Execute("GetValues", ANY.to_any(None)))[0]

        # print
        if self.debug:
            print('%s: %s'%(var_name, val))

        return val


    def set_var(self, var_name='v_name', val='write_0'):
        s = "@GLOBAL_VARS/" + var_name
        tv_name = self.task.GetVariable(s, "")
        tv_name.Execute("SetValues", ANY.to_any([[["value", unicode(str(val))]]]))

        # print
        if self.debug:
            self.get_var(var_name)  # check


    def set_var_socket(self, var, val):
        msg = str(var)+":"+str(val)
        self.skt.send(msg.encode("utf-8"))
        print(f"sent '{msg}'")
        return


if __name__ == "__main__":
    nx_ip="192.168.0.23"
    nx_if = NextageNXAInterface(ip=nx_ip, debug=True)
    nx_if.setup()
    nx_if.get_var("nextage_status")
