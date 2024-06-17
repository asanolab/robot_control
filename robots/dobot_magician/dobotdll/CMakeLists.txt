cmake_minimum_required(VERSION 2.8.3)
project(dobotdll)

find_package(catkin REQUIRED COMPONENTS
)

find_package(Qt5 REQUIRED COMPONENTS
  Core
  Network
  SerialPort
)

catkin_package(
  INCLUDE_DIRS   src
  LIBRARIES      ${PROJECT_NAME}
  CATKIN_DEPENDS
  DEPENDS        Qt5Core Qt5Network Qt5SerialPort
)

qt5_wrap_cpp(QT_MOC_SRCS
  src/CDobotCommunicator.h
  src/CDobotConnector.h
  src/CDobot.h
  src/CDobotProtocol.h
  src/DobotDevice/UdpPort.h
  src/DobotDevice/UdpSearch.h
)

add_library(${PROJECT_NAME}
  src/CDobotCommunicator.cpp
  src/CDobotConnector.cpp
  src/CDobot.cpp
  src/CDobotProtocol.cpp
  src/DobotDll.cpp
  src/ComPlatform/Message.cpp
  src/ComPlatform/Packet.cpp
  src/ComPlatform/RingBuffer.cpp
  src/DobotDevice/UdpPort.cpp
  src/DobotDevice/UdpSearch.cpp
  ${QT_MOC_SRCS}
)

target_include_directories(${PROJECT_NAME} PRIVATE src src/ComPlatform)
qt5_use_modules(${PROJECT_NAME} Core Network SerialPort)
