# robot_control

## Install & Build
- Install ROS
  - https://github.com/asanolab/handbook/tree/main/install_doc/ROS  
- Workspace setup
  - https://github.com/asanolab/handbook/blob/main/install_doc/workspace.md  

Clone the repository and install dependencies
```
git clone https://github.com/asanolab/robot_control.git
rosdep install -y -r --from-paths robot_control --ignore-src
```

Build
```
cd robot_control/robot_control
catkin bt
```
