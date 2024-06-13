cmake_minimum_required(VERSION 2.8.0)
project(panda)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  xacro
  roseus
  )
find_package(panda_eus)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs
  )


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


#############
## Install ##
#############

install(DIRECTORY models euslisp launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS)
