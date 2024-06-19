# lite6_interface
Software for UFactory Lite6

# Build
```
cd ufactory_arm
catkin bt
```

# Demo
## Moveit (interactive)
```
roslaunch lite6_moveit_config demo.launch
```

## Moveit (motion by command)
```
roslaunch lite6_moveit_config demo.launch
rosrun lite6_interface test_manip_lite6.py
```
![lite6_moveit](https://github.com/asanolab/robot_control/assets/6872136/632aa2d6-1aec-4f7b-83ef-2bf6f9e58d08)
