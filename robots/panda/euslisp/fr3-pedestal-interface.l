(require :fr3-interface "package://panda/euslisp/fr3-interface.l")
(require :fr3-pedestal "package://panda/euslisp/models/fr3-pedestal.l")

(defclass fr3-pedestal-robot-interface
  :super fr3-robot-interface
  :slots ()
  )

(defmethod fr3-pedestal-robot-interface
  (:init
   (&rest args &key ((:controller-timeout ct) nil))
   (send-super* :init args)
   )
  )

(defun fr3-pedestal-init ()
  (setq *ri* (instance fr3-pedestal-robot-interface :init))
  (setq *robot* (fr3_pedestal))
  (setq *fr3* *fr3_pedestal*)
  )
