cmake_minimum_required(VERSION 2.8.0)
project(dobot_magician)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  )

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs
  )

# add_message_files(
#   FILES
#   )

# generate_messages(
#   DEPENDENCIES
#   std_msgs
#   )
