#!/usr/bin/env roseus

(ros::roseus "fr3_bringup")
(load "package://panda/euslisp/fr3-interface.l")

(fr3-init)
(objects (list *robot*))
