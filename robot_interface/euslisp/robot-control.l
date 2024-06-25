;; robot-control class

(defclass robot-control-base
  :super propertied-object
  :slots (mt-default ll-default)
  )

(defmethod robot-control-base
  (:init
   ()
   (setq mt-default (send *robot* :larm :end-coords))
   (setq ll-default (send *robot* :link-list (send (send *robot* :larm :end-coords) :parent)))
   )
  (:solve-ik-base
   (&key
    tgc
    (mt mt-default)
    (ll ll-default)
    (ta t)
    (ra t)
    (thre 1.0)
    (rthre (deg2rad 1.0))
    (rif nil)
    (dv nil)
    (stop 250)
    (wue nil)
    (run nil)
    (time 5000)
    (cartesian nil)
    )
   (send *robot* :inverse-kinematics tgc
         :move-target mt
         :link-list ll
         :translation-axis ta
         :rotation-axis ra
         :thre thre
         :rthre (deg2rad rthre)
         :revert-if-fail rif
         :debug-view dv
         :stop stop
         )
   (send *irtviewer* :draw-objects)
   (when wue (send self :wait-until-enter))
   (when run (send self :move (send *robot* :angle-vector) time :cartesian cartesian))
   )
  ;;
  (:move
   (send-av time &key (cartesian nil))
   (when cartesian
     (setq time (* 10 time))  ;; bug? this is necessary when moving robot with :end-coords-interpolation t
     )
   (send *ri* :angle-vector send-av time nil 0 :end-coords-interpolation cartesian)
   (send *ri* :wait-interpolation))
  (:move-cartesian
   (send-av time)
   (send self :move send-av time :cartesian t))
  ;;
  (:wait-until-enter
   ()
   (format t "press enter to next step~%")
   (do-until-key
    (x::window-main-one)))
  )


;; lleg
(defclass robot-control-lleg
  :super robot-control-base
  :slots ()
  )

(defmethod robot-control-lleg
  (:init
   (&rest args)
   (send-super* :init args)
   )
  (:solve-ik-lleg
   (&rest args)
   (send-super* :solve-ik-base
         :mt (send *robot* :lleg :end-coords)
         :ll (send *robot* :link-list (send (send *robot* :lleg :end-coords) :parent))
         args)
   )
  )

;; rleg
(defclass robot-control-rleg
  :super robot-control-base
  :slots ()
  )

(defmethod robot-control-rleg
  (:init
   (&rest args)
   (send-super* :init args)
   )
  (:solve-ik-rleg
   (&rest args)
   (send-super* :solve-ik-base
         :mt (send *robot* :rleg :end-coords)
         :ll (send *robot* :link-list (send (send *robot* :rleg :end-coords) :parent))
         args)
   )
  )
