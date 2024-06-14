cmake_minimum_required(VERSION 2.8.0)
project(franka_arm)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  )
find_package(panda_eus)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs
  )


###
### fr3.l generation
###
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.l
  COMMAND rosrun euscollada collada2eus -I ${PROJECT_SOURCE_DIR}/models/fr3.urdf -C fr3.yaml -O fr3.l
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/euslisp/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/fr3.urdf ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.yaml)

add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/models/fr3.urdf
  COMMAND rosrun xacro xacro --inorder fr3.urdf.xacro > ${PROJECT_SOURCE_DIR}/models/fr3.urdf
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/fr3.urdf.xacro)

add_custom_target(generate_fr3_lisp ALL DEPENDS ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.l)


###
### panda-pedestal.l generation
###
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/euslisp/models/panda-pedestal.l
  COMMAND rosrun euscollada collada2eus -I ${PROJECT_SOURCE_DIR}/models/panda_pedestal.urdf -C ${panda_eus_SOURCE_PREFIX}/models/panda.yaml -O panda-pedestal.l
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/euslisp/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/panda_pedestal.urdf ${panda_eus_SOURCE_PREFIX}/models/panda.yaml)

add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/models/panda_pedestal.urdf
  COMMAND rosrun xacro xacro --inorder panda_pedestal.urdf.xacro > panda_pedestal.urdf
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/panda_pedestal.urdf.xacro)

add_custom_target(generate_panda-pedestal_lisp ALL DEPENDS ${PROJECT_SOURCE_DIR}/euslisp/models/panda-pedestal.l)


###
### fr3-pedestal.l generation
###
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/euslisp/models/fr3-pedestal.l
  COMMAND rosrun euscollada collada2eus -I ${PROJECT_SOURCE_DIR}/models/fr3_pedestal.urdf -C ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.yaml -O fr3-pedestal.l
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/euslisp/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/fr3_pedestal.urdf ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.yaml)

add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/models/fr3_pedestal.urdf
  COMMAND rosrun xacro xacro --inorder fr3_pedestal.urdf.xacro > fr3_pedestal.urdf
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/fr3_pedestal.urdf.xacro)

add_custom_target(generate_fr3-pedestal_lisp ALL DEPENDS ${PROJECT_SOURCE_DIR}/euslisp/models/fr3-pedestal.l)


###
### panda-expriment.l generation
###
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/euslisp/models/panda-experiment.l
  COMMAND rosrun euscollada collada2eus -I ${PROJECT_SOURCE_DIR}/models/panda_experiment.urdf -C ${panda_eus_SOURCE_PREFIX}/models/panda.yaml -O panda-experiment.l
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/euslisp/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/panda_experiment.urdf ${panda_eus_SOURCE_PREFIX}/models/panda.yaml)

add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/models/panda_experiment.urdf
  COMMAND rosrun xacro xacro --inorder panda_experiment.urdf.xacro > panda_experiment.urdf
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/panda_experiment.urdf.xacro)

add_custom_target(generate_panda-experiment_lisp ALL DEPENDS ${PROJECT_SOURCE_DIR}/euslisp/models/panda-experiment.l)


###
### fr3-expriment.l generation
###
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/euslisp/models/fr3-experiment.l
  COMMAND rosrun euscollada collada2eus -I ${PROJECT_SOURCE_DIR}/models/fr3_experiment.urdf -C ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.yaml -O fr3-experiment.l
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/euslisp/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/fr3_experiment.urdf ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.yaml)

add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/models/fr3_experiment.urdf
  COMMAND rosrun xacro xacro --inorder fr3_experiment.urdf.xacro > fr3_experiment.urdf
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/models
  DEPENDS ${PROJECT_SOURCE_DIR}/models/fr3_experiment.urdf.xacro)

add_custom_target(generate_fr3-experiment_lisp ALL DEPENDS ${PROJECT_SOURCE_DIR}/euslisp/models/fr3-experiment.l)



#############
## Install ##
#############

install(DIRECTORY models euslisp launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS)
