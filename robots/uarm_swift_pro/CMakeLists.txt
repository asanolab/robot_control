cmake_minimum_required(VERSION 2.8.0)
project(uarm_swift_pro)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  )

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
  )

# add_message_files(
#   FILES
#   SwiftproState.msg
#   )

# generate_messages(
#   DEPENDENCIES
#   std_msgs
#   )
