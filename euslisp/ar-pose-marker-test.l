#!/usr/bin/env roseus

(ros::roseus-add-msgs "ar_track_alvar_msgs")

;; use ar_pose_marker
;; /ar_pose_marker: marker -> camera transform
(defun ar-marker-cb (msg)
  (let (cam->marker-coords cam-coords)
    ;; (send msg :markers)で取れる複数マーカ情報をar-merkerにセットしながら処理.
    (mapcar #'(lambda (ar-marker)
                (let* ((cam->marker-coords (ros::tf-pose->coords (send ar-marker :pose :pose)))
                       (cam-coords (send (send *panda* :camera1_color_optical_frame_lk) :copy-worldcoords)))
                  (send *target-marker* :newcoords (send cam-coords :transform cam->marker-coords))
                  ))
            (send msg :markers))
    ))

(ros::subscribe "/ar_pose_marker" ar_track_alvar_msgs::AlvarMarkers #'ar-marker-cb)



(defun main ()
  (ros::rate 10)
  (do-until-key
   (ros::spin-once)
   (send *irtviewer* :draw-objects)
   (x::window-main-one)
   (ros::sleep)
   ))

(main)
