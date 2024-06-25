#!/usr/bin/env roseus

(ros::roseus "ar_marker_util")

(setq *tfl* (instance ros::transform-listener :init))


;; use tf
;; /tf: camera -> marker transform
(defun get-cam-to-marker-coords (cam-coords camera-frame-name target-marker)
  (let (cam->marker-coords
        stamp
        marker-name)
    (setq stamp (ros::time-now))
    (setq marker-name (send target-marker :name))
    (when (send *tfl* :wait-for-transform camera-frame-name marker-name stamp 5)
      (setq cam->marker-coords (send *tfl* :lookup-transform camera-frame-name marker-name stamp))
      (send target-marker :newcoords (send cam-coords :transform cam->marker-coords))
      )))
