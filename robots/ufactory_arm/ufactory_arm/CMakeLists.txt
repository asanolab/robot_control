cmake_minimum_required(VERSION 2.8.0)
project(ufactory_arm)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  )

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs
  )
