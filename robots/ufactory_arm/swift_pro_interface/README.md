# References
- API (github)
  - https://github.com/uArm-Developer/RosForSwiftAndSwiftPro

# Install

```bash
catkin bt
```

# Rviz only

```
roslaunch swift_pro_interface swift_pro_display.launch
```

# Manipulation demo
```
roslaunch swift_pro_interface swift_pro_control.launch
roslaunch pro_moveit_config demo.launch

cd scripts
./test_manip.py
```

# Pump
```
roslaunch swift_pro_interface swift_pro_control.launch

cd scripts
./test_pump_on.py   # pump on
./test_pump_off.py  # pump off
```