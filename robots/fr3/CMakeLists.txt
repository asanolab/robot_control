cmake_minimum_required(VERSION 2.8.0)
project(fr3)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  euscollada
  roseus
  xacro
  )

find_package(franka_description)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs
  )


###
### fr3.l generation
###
set(_fr3_xacro ${franka_description_SOURCE_PREFIX}/robots/fr3/fr3.urdf.xacro)  # franka_description is installed from source
if(NOT EXISTS ${_fr3_xacro})
  set(_fr3_xacro ${franka_description_PREFIX}/share/franka_description/robots/fr3/fr3.urdf.xacro)  # franka_description is installed from apt
endif()
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.l
  COMMAND rosrun euscollada collada2eus -I fr3.urdf -C fr3.yaml -O fr3.l
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/euslisp/models
  DEPENDS ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.urdf ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.yaml)
add_custom_command(OUTPUT ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.urdf
  COMMAND rosrun xacro xacro --inorder ${_fr3_xacro} hand:=true > ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.urdf
  DEPENDS ${_fr3_xacro})

add_custom_target(generate_fr3_lisp ALL DEPENDS ${PROJECT_SOURCE_DIR}/euslisp/models/fr3.l)


#############
## Install ##
#############

install(DIRECTORY euslisp
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS)
