#!/usr/bin/env roseus

(ros::roseus "panda_experiment_bringup")
(load "package://panda/euslisp/panda-experiment-interface.l")

(panda-experiment-init)
(objects (list *robot*))
