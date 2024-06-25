(setq *test* (make-cube 10 10 10 :name "test"))

(defmacro generate-coords (coords-name base-object offset-xyz offset-rpy)
  ;; coords-name: name of coords to be generated
  ;; base-object: coords of the object will be used for offset transform
  ;; offset-xyz : 3dof vector [mm]
  ;; offset-rpy : 3dof vector [deg]
  (unless (vectorp offset-xyz)
    (return-from generate-coords (warn "offset-xyz should be a vector~%")))
  (unless (vectorp offset-rpy)
    (return-from generate-coords (warn "offset-rpy should be a vector~%")))
  `(setq ,coords-name
        (make-coords
         :pos (v+ (send ,base-object :worldpos) ,offset-xyz)
         :rot (rotate-matrix
               (rotate-matrix
                (rotate-matrix
                 (send ,base-object :rot)
                 (deg2rad (elt ,offset-rpy 2)) :z nil)
                 (deg2rad (elt ,offset-rpy 1)) :y nil)
                 (deg2rad (elt ,offset-rpy 0)) :x nil)
         ))
  )

(generate-coords *coords_1* *test* #f(10 10 10) #(-2 -3 -4))
