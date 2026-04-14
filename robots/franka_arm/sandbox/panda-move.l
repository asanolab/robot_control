#!/usr/bin/env roseus

(ros::roseus "panda_move")
(load "package://panda_eus/euslisp/panda-interface.l")

(panda-init)
(objects (list *robot*))

(setq *js* nil)

(defun joint-states-cb (msg)
  (setq *js* msg)
  (update-eusmodel-with-jointstates *js*)
  )

(ros::subscribe "/joint_states" sensor_msgs::JointState #'joint-states-cb)

(defun update-eusmodel-with-jointstates (joint-states)
  (let ((update-av (send *panda* :angle-vector)))
    (dotimes (i (length (send joint-states :name)))
      (cond
       ((equal (elt (send joint-stetes :name) i) "panda_joint1")
        (setf (aref update-av 0) (rad2deg (elt (send joint-stetes :position) i))))
       ((equal (elt (send joint-stetes :name) i) "panda_joint2")
        (setf (aref update-av 1) (rad2deg (elt (send joint-stetes :position) i))))
       ((equal (elt (send joint-stetes :name) i) "panda_joint3")
        (setf (aref update-av 2) (rad2deg (elt (send joint-stetes :position) i))))
       ((equal (elt (send joint-stetes :name) i) "panda_joint4")
        (setf (aref update-av 3) (rad2deg (elt (send joint-stetes :position) i))))
       ((equal (elt (send joint-stetes :name) i) "panda_joint5")
        (setf (aref update-av 4) (rad2deg (elt (send joint-stetes :position) i))))
       ((equal (elt (send joint-stetes :name) i) "panda_joint6")
        (setf (aref update-av 5) (rad2deg (elt (send joint-stetes :position) i))))
       ((equal (elt (send joint-stetes :name) i) "panda_joint7")
        (setf (aref update-av 6) (rad2deg (elt (send joint-stetes :position) i))))
       )
      )
    (send *panda* :angle-vector update-av)
    ))

(defun get-joint-id-by-name (joint-states joint-name)
  (let (i joint-id)
    (dotimes (i (length (send joint-states :name)))
      (if (equal (elt (send joint-states :name) i) joint-name)
          (setq joint-id i))
      )
    joint-id))


(defun main (&key (run nil))
  (do-until-key
   (ros::spin-once)
   (x::window-main-one)
   (send *irtviewer* :draw-objects)
   (when run
     (send *ri* :angle-vector (send *panda* :angle-vector))
     ;;(send *ri* :wait-interpolation)
     ;;(unix::usleep (* 5000 1000))
     )))

(main :run nil)

