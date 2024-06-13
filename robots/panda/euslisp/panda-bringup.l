#!/usr/bin/env roseus

(ros::roseus "panda_bringup")
(load "package://panda_eus/euslisp/panda-interface.l")

(panda-init)
(objects (list *robot*))
