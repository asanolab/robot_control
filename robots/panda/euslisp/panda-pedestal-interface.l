(require :robot-interface "package://panda_eus/euslisp/panda-interface.l")
(require :panda-pedestal "package://panda/euslisp/models/panda-pedestal.l")

(defclass panda-pedestal-robot-interface
  :super panda-robot-interface
  :slots ()
  )

(defmethod panda-pedestal-robot-interface
  (:init
   (&rest args &key ((:controller-timeout ct) nil))
   (send-super* :init args)
   )
  )

(defun panda-pedestal-init ()
  (setq *ri* (instance panda-pedestal-robot-interface :init))
  (setq *robot* (panda_pedestal))
  (setq *panda* *panda_pedestal*)
  )
