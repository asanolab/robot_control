#!/usr/bin/env roseus

(ros::roseus "fr3_bringup")
(load "package://franka_arm/euslisp/fr3-interface.l")

(fr3-init)
(objects (list *robot*))
