#!/usr/bin/env roseus

;; robotの初期化
(load "package://panda_eus/euslisp/panda-interface.l")
(load "package://franka_robot_control/models/panda-press.l")
(load "package://robot_interface/euslisp/ar-marker-util.l")

(ros::roseus "ar_marker_node")


;;memo
;; access x pos
;; (send (elt (send m :markers) 0) :pose :pose :position :x)
;; access id
;; (send (car (send m :markers)) :id)
;; get number of marker
;; (length (send msg :markers))

;;; 表示モデルなど
;; coldpress
(setq *ar-marker-0* (make-cube 45 45 2 :name "/ar_marker_0"))
(send *ar-marker-0* :set-color :yellow)
(send *ar-marker-0* :locate #f(-250 650 1100))
;; heatpress
(setq *ar-marker-1* (make-cube 45 45 2 :name "/ar_marker_1"))
(send *ar-marker-1* :set-color :yellow)
(send *ar-marker-1* :locate #f(200 650 1100))
;; plate top
(setq *ar-marker-2* (make-cube 45 45 2 :name "/ar_marker_2"))
(send *ar-marker-2* :set-color :yellow)
;; plate middle
(setq *ar-marker-3* (make-cube 45 45 2 :name "/ar_marker_3"))
(send *ar-marker-3* :set-color :yellow)
;; plate bottom
(setq *ar-marker-4* (make-cube 45 45 2 :name "/ar_marker_4"))
(send *ar-marker-4* :set-color :yellow)
(send *ar-marker-4* :locate #f(700 0 950))
;; plate cutter
(setq *ar-marker-5* (make-cube 45 45 2 :name "/ar_marker_5"))
(send *ar-marker-5* :set-color :yellow)
;; polymer cup
(setq *ar-marker-6* (make-cube 45 45 2 :name "/ar_marker_6"))
(send *ar-marker-6* :set-color :yellow)
;; polymer cup2
(setq *ar-marker-7* (make-cube 45 45 2 :name "/ar_marker_7"))
(send *ar-marker-7* :set-color :yellow)
;; fork
(setq *ar-marker-8* (make-cube 45 45 2 :name "/ar_marker_8"))
(send *ar-marker-8* :set-color :yellow)

(if (not (boundp '*panda*))
    (panda-init)
  )

(if (not (boundp '*irtviewer*))
    (progn
      (make-irtviewer)
      (objects (list
                *ar-marker-0*
                *ar-marker-1*
                *ar-marker-2*
                *ar-marker-3*
                *ar-marker-4*
                *ar-marker-5*
                *ar-marker-6*
                *ar-marker-7*
                *ar-marker-8*
                *panda*)))
  )

(defun get-panda-cam-to-marker-coords (target-marker)
  (let ((cam-coords (send (send *panda* :camera1_color_optical_frame_lk) :copy-worldcoords))
        (camera-frame-name "camera1_color_optical_frame"))
    (get-cam-to-marker-coords cam-coords camera-frame-name target-marker)))
