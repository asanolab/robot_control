# References
- github
  - https://github.com/uArm-Developer/RosForSwiftAndSwiftPro


# Install

```bash
cd ~/catkin_ws/src/robot_control/robots/uarm_swift_pro
wstool merge -t ~/catkin_ws/src install/uarm_swift_pro.<rosdistro>.rosinstall
wstool update

rosdep install -y -r --from-paths . --ignore-src
catkin build
```

# Rviz only

```
roslaunch uarm_swift_pro swift_pro_display.launch
```

# Manipulation demo
```
roslaunch uarm_swift_pro swift_pro_control.launch
roslaunch pro_moveit_config demo.launch
./uarm_swift_pro_sample.py
```

# Pump
```
roslaunch uarm_swift_pro swift_pro_control.launch

cd scripts
./test_pump_on.py   # pump on
./test_pump_off.py  # pump off
```