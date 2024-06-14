(require :robot-interface "package://panda_eus/euslisp/panda-interface.l")
(require :panda-experiment "package://franka_arm/euslisp/models/panda-experiment.l")

(defclass panda-experiment-robot-interface
  :super panda-robot-interface
  :slots ()
  )

(defmethod panda-experiment-robot-interface
  (:init
   (&rest args &key ((:controller-timeout ct) nil))
   (send-super* :init args)
   )
  )

(defun panda-experiment-init ()
  (setq *ri* (instance panda-experiment-robot-interface :init))
  (setq *robot* (panda_experiment))
  (setq *panda* *panda_experiment*)
  )
