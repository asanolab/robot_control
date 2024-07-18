cmake_minimum_required(VERSION 2.8.0)
project(lite6_interface)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  xarm_msgs
  )

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS scripts/test_gripper_lite6.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
