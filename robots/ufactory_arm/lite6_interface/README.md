# lite6_interface
Software for UFactory Lite6

## References
  - API (github)
    - https://github.com/xArm-Developer/xarm_ros.git

## Setup 
### Workspace setup
- Create workspace before start
  - https://github.com/asanolab/robot_control

- Workspace setup and build
```bash
cd lite6_interface
wstool merge -t ~/catkin_ws/src/ install/lite6_interface.noetic.rosinstall 
wstool update
rosdep install -y -r --from-paths . --ignore-src

catkin bt
```

# Demo
## Manipulation (moveit)
- Simulation
```
roslaunch lite6_moveit_config demo.launch  # interactive planning in rviz

rosrun lite6_interface test_manip_lite6.py  # sample motion by command
```
![lite6_moveit](https://github.com/asanolab/robot_control/assets/6872136/632aa2d6-1aec-4f7b-83ef-2bf6f9e58d08)

- Real robot motion
```
roslaunch lite6_moveit_config realMove_exec.launch robot_ip:=192.168.0.42 uf_hw_ns:=lite6 add_gripper:=true  # use ip address of the robot
rosrun lite6_interface test_manip_lite6.py
```

## Gripper motion
```
rosrun lite6_interface test_gripper_lite6.py
```

or directly call rosservice
```
rosservice call /lite6/vacuum_gripper_set 1  # open
rosservice call /lite6/vacuum_gripper_set 0  # close
```
