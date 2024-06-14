#!/usr/bin/env roseus

(ros::roseus "fr3_pedestal_bringup")
(load "package://franka_arm/euslisp/fr3-pedestal-interface.l")

(fr3-pedestal-init)
(objects (list *robot*))
