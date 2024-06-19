# swiftpro_interface
Software for uArm SwiftPro

# References
- API (github)
  - https://github.com/uArm-Developer/RosForSwiftAndSwiftPro

# Build
```bash
catkin bt
```

# Visualization (Rviz)
```
roslaunch swiftpro_interface swiftpro_display.launch
```
![swiftpro_rviz](https://github.com/asanolab/robot_control/assets/6872136/b7330b9b-67e6-4da3-8f43-22b92f66f00f)


# Demo
## Manipulation (moveit)
### Interactive
```
roslaunch pro_moveit_config demo.launch
```

### By command
```
roslaunch swiftpro_interface swiftpro_moveit_manip.launch
rosrun swiftpro_interface test_manip_swiftpro.py
```
![swiftpro_moveit](https://github.com/asanolab/robot_control/assets/6872136/b9810777-de69-430a-a857-f341f8551f21)


## Pump
```
roslaunch swiftpro_interface swiftpro_bringup.launch

cd scripts
./test_pump_on.py   # pump on
./test_pump_off.py  # pump off
```
