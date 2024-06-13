#!/usr/bin/env roseus

(ros::roseus "panda_pedestal_bringup")
(load "package://panda/euslisp/panda-pedestal-interface.l")

(panda-pedestal-init)
(objects (list *robot*))
