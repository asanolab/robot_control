# Install
```
cd lite6
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