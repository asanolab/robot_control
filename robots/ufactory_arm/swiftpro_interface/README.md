# References
- API (github)
  - https://github.com/uArm-Developer/RosForSwiftAndSwiftPro

# Install
```bash
catkin bt
```

# Visualization (Rviz)
```
roslaunch swiftpro_interface swiftpro_display.launch
```

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

## Pump
```
roslaunch swiftpro_interface swiftpro_bringup.launch

cd scripts
./test_pump_on.py   # pump on
./test_pump_off.py  # pump off
```