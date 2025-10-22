#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# memo
# - authority is needed for write by changing display line to yellow (read is not need)
# - u'' is not necessary in python3 (python2 needs)

## NEXTAGE
from omniORB import CORBA, any as ANY
from NxApi import *

#variables:
# - thickness_counter
# - micrometer_counter
# - sample_assemble_counter
# - sample_set_counter
# - sample_disassemble_counter


class NextageNXAInterface():
    def __init__(self, nx_ip="192.168.0.10", debug=True):
        self.ipaddr_str = nx_ip
        self.argv = ["-ORBdefaultWCharCodeSet", "UTF-16", "-ORBgiopMaxMsgSize", "104857600"]

        # Connect to the API servern
        self.orb = CORBA.ORB_init(self.argv, CORBA.ORB_ID)
        self.api = self.orb.string_to_object(
            "corbaloc:iiop:1.2@%s:2809/RootControllerApi" % (self.ipaddr_str)
        )

        self.root_controller = self.api._narrow(RootNxController)

        # Raising an exception if the maximum number of clients is reached
        self.controller = self.root_controller.GetNxController("", "")

        # Get Variable's variable values
        self.task = self.controller.GetNxObject(u"Task", u"")
        self.varlist= ANY.from_any(self.task.GetVariableNames(u"@GLOBAL_VARS"))

        self.debug = debug

        if self.debug:
            print("Task Name: '%s'"%(self.task.Name))
            print("varlist: '%s'"%(self.varlist))


    # Acquire API Authority
    def get_authority(self):
        self.controller.Execute("GetAuthority", ANY.to_any(None))


    # Release API authority
    def release_authority(self):
        self.controller.Execute("ReleaseAuthority", ANY.to_any(None))


    def get_variable(self, variable_name='v_name'):
        s = "@GLOBAL_VARS/" + variable_name
        tv_name = self.task.GetVariable(s, "")  # task_variable_name

        value = ANY.from_any(tv_name.Execute("GetValues", ANY.to_any(None)))[0]

        # print
        if self.debug:
            print('%s: %s'%(variable_name, value))

        return value


    def set_variable(self, variable_name='v_name', variable_value='write_0'):
        self.get_authority()

        s = "@GLOBAL_VARS/" + variable_name
        tv_name = self.task.GetVariable(s, "")
        tv_name.Execute("SetValues", ANY.to_any([[["value", variable_value]]]))

        # print
        if self.debug:
            self.get_variable(variable_name)  # check

        self.release_authority()



if __name__ == "__main__":
    ip="192.168.0.23"
    nx_if = NextageNXAInterface(nx_ip=ip, debug=True)
    nx_if.get_variable("nextage_status")
    nx_if.get_variable("tma_status")
    nx_if.get_variable("sample_set_counter")
    nx_if.get_variable("sample_get_counter")
    nx_if.get_variable("thickness_counter")
    nx_if.get_variable("micrometer_counter")

    nx_if.set_variable("thickness_counter", "4")
