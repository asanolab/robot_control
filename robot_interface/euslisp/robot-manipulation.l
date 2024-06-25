(load "package://robot_interface/euslisp/robot-control.l")

;; larm
(defclass robot-manipulation-larm
  :super robot-control-base
  :slots ()
  )

(defmethod robot-manipulation-larm
  (:init
   (&rest args)
   (send-super* :init args)
   )
  (:solve-ik-larm
   (&rest args)
   (send-super* :solve-ik-base
         :mt (send *robot* :larm :end-coords)
         :ll (send *robot* :link-list (send (send *robot* :larm :end-coords) :parent))
         args)
   )
  )

;; rarm
(defclass robot-manipulation-rarm
  :super robot-control-base
  :slots ()
  )

(defmethod robot-manipulation-rarm
  (:init
   (&rest args)
   (send-super* :init args)
   )
  (:solve-ik-rarm
   (&rest args)
   (send-super* :solve-ik-base
         :mt (send *robot* :rarm :end-coords)
         :ll (send *robot* :link-list (send (send *robot* :rarm :end-coords) :parent))
         args)
   )
  ;;[todo]
  ;; - define higher level
 (:solve-ik-rarm-relative
  (diff)
  ;; link setting
  (setq mt (send *robot* :rarm :end-coords))
  (setq ll (send *robot* :link-list (send (send *robot* :rarm :end-coords) :parent)))
  ;; tgc
  (setq tgc-now (send (send *robot* :rarm :end-coords) :copy-worldcoords))
  (setq ec-pos-now (send tgc-now :worldpos))
  (setq tgc-pos-new (v+ ec-pos-now diff))
  (setq tgc-new (send tgc-now :locate tgc-pos-new :world))
  ;; ik
  (send *robot* :inverse-kinematics tgc-new
        :move-target mt
        :link-list ll
        ;;:translation-axis ta
        ;;:rotation-axis ra
        ;;:thre thre
        ;;:rthre (deg2rad rthre)
        ;;:revert-if-fail rif
        ;;:debug-view dv
        ;;:stop stop
        )
  )
  ;;
  ;; for grasp
  ;; [todo]
  ;; - grasp related should be separated common part and arm(lr) specific part
  (:grasp-tool
   (&key (width 0.005) (time 1000) (effort 10.0) (wait t) (inner 0.002) (outer 0.002))
   ;; width: width of grasp object [m]
   ;; time : speed of grasp outside to inside [m/s]
   ;; inner: inner tolerance [m]
   ;; outer: outer tolerance [m]
   (let (_isGraspSuccess)
     (send *ri* :start-grasp :rarm :width width :tm time :effort effort :wait wait :inner inner :outer outer)
     (setq _isGraspSuccess (send (send *ri* :get-start-grasp-result :rarm) :success))
     (if _isGraspSuccess
         (print "grasp success")
       (progn
         (print "grasp fail")
         (send *ri* :stop-grasp :arm))
       )
     _isGraspSuccess))
  (:grasp-tool-cb
   (msg)
   (format t "/grasp_tool: ~A~%" (send msg :data))
   (if (send msg :data)
       (send self :grasp-tool))
   )
  (:release-tool
   ()
   (send *ri* :stop-grasp :arm)
   (send *ri* :wait-interpolation)
   )
  (:release-tool-cb
   (msg)
   (format t "/release_tool: ~A~%" (send msg :data))
   (if (send msg :data)
       (send self :release-tool))
   )
  (:reset-gripper
   ()
   (send *ri* :homing-gripper :arm))
  (:reset-gripper-cb
   (msg)
   (format t "/reset_gripper: ~A~%" (send msg :data))
   (if (send msg :data)
       (send self :reset-gripper))
   )
  ;;
  ;; for pick & place
  ;; general base function
  (:pick-object-base
   (pick-obj coords-list time-list
             &key (grasp-timing nil)
             (grasp-width 0.005) (grasp-time 500) (grasp-effort 10) (grasp-inner 0.002) (grasp-outer 0.002)
             (skip-gripper nil)
             (cartesian nil))
   (let (cn tn num-cl)
     (setq num-cl (length coords-list)) ;; num-cl: number of coords-list
     (dotimes (i num-cl)
       ;; gripper motion is executed before the pose of index i
       (when (equal i grasp-timing)
         (when (and run (not skip-gripper))
           (send self :grasp-tool :width grasp-width :time grasp-time :effort grasp-effort :inner grasp-inner :outer grasp-outer))
         (when pick-obj
           (send (car (last (send *robot* :rarm :links))) :assoc pick-obj)))
       (setq cn (elt coords-list i))
       (setq tn (elt time-list i))
       (send self :solve-ik-rarm :tgc cn :wue wue :run run :time tn :cartesian cartesian))
     ;; if gripper motion is appropriate after the last pose
     (if (equal num-cl grasp-timing)
         (send self :grasp-tool :width grasp-width :time grasp-time :effort grasp-effort :inner grasp-inner :outer grasp-outer))
     ))
  (:place-object-base
   (place-obj coords-list time-list
              &key (release-timing nil) (place-on nil)
              (skip-gripper nil)
              (cartesian nil))
   (let (cn tn)
     (setq num-cl (length coords-list)) ;; num-cl: number of coords-list
     (dotimes (i num-cl)
       ;; gripper motion is executed before the pose of index i
       (when (equal i release-timing)
         (when (and run (not skip-gripper))
           (send *ri* :stop-grasp :rarm)
           (send *ri* :wait-interpolation))
         (send (car (last (send *robot* :rarm :links))) :dissoc place-obj)
         (when place-on
           (send place-on :assoc place-obj))
         )
       (setq cn (elt coords-list i))
       (setq tn (elt time-list i))
       (send self :solve-ik-rarm :tgc cn :wue wue :run run :time tn :cartesian cartesian))
     ;; if gripper motion is appropriate after the last pose
     (if (equal num-cl release-timing)
         (progn
           (send *ri* :stop-grasp :rarm)
           (send *ri* :wait-interpolation)))
     ))
  )
