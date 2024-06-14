#!/usr/bin/env roseus

(ros::roseus "fr3_experiment_bringup")
(load "package://panda/euslisp/fr3-experiment-interface.l")

(fr3-experiment-init)
(objects (list *robot*))
