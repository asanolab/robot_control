# robot_control

## Install & Build
Install ROS
- melodic
  - https://wiki.ros.org/melodic/Installation/Ubuntu
- noetic
  - https://wiki.ros.org/noetic/Installation/Ubuntu 

Workspace setup
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
wstool init .
catkin build
```

Clone the repository and install dependencies
```
git clone https://github.com/asanolab/robot_control.git
rosdep install -y -r --from-paths robot_control --ignore-src
```

Build
```
cd robot_control/robot_control
git submodule update --init --recursive
catkin bt
```
