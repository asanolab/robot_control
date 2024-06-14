(require :fr3-interface "package://panda/euslisp/fr3-interface.l")
(require :fr3-experiment "package://panda/euslisp/models/fr3-experiment.l")

(defclass fr3-experiment-robot-interface
  :super fr3-robot-interface
  :slots ()
  )

(defmethod fr3-experiment-robot-interface
  (:init
   (&rest args &key ((:controller-timeout ct) nil))
   (send-super* :init args)
   )
  )

(defun fr3-experiment-init ()
  (setq *ri* (instance fr3-experiment-robot-interface :init))
  (setq *robot* (fr3_experiment))
  (setq *fr3* *fr3_experiment*)
  )
