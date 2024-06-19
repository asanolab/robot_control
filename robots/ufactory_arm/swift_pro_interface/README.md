# References
- API (github)
  - https://github.com/uArm-Developer/RosForSwiftAndSwiftPro

# Install
```bash
catkin bt
```

# Visualization (Rviz)
```
roslaunch swift_pro_interface swift_pro_display.launch
```

# Demo
## Manipulation (moveit)
### Interactive
```
roslaunch pro_moveit_config demo.launch
```

### By command
```
roslaunch swift_pro_interface swift_pro_moveit_manip.launch
rosrun swift_pro_interface test_manip_swiftpro.py
```

## Pump
```
roslaunch swift_pro_interface swift_pro_bringup.launch

cd scripts
./test_pump_on.py   # pump on
./test_pump_off.py  # pump off
```