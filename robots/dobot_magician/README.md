# Setup
## Requirement
- Magician_ROS
  - officially provided from the Dobot-Arm pkg
  - https://github.com/Dobot-Arm/Magician_ROS
- dobotdll (from DobotDemoV2.0)
  - V2.0 is compatible with Magician_ROS
  - V2.3 (latest version) which can be downloaded from the download center, V2.2 and V2.1 are not compatible with Magician_ROS
    - Download center -> https://www.dobot-robots.com/service/download-center?keyword=&products%5B%5D=316

# Install
```
cd dobot_magician
catkin bt
```

# Demo
## moveit (interactive)
```
roslaunch dobot_magician_moveit_config demo.launch
```
![dobot_magician_moveit](https://github.com/asanolab/robot_control/assets/6872136/681fda1f-63ea-4560-aeaf-431f8169971f)

## moveit (motion by commands)
```
roslaunch dobot_magician_moveit_config demo.launch
rosrun dobot_magician_interface test_manip_dobot_magician.py
```

# memo
- python3 is assumed to be used

- rviz
![Screenshot from 2024-04-24 12-15-38](https://github.com/asanolab/robot_control/assets/6872136/55eaee9e-4a92-48e4-8b6f-8c7cceed6b15)

- gazebo
![dobot_magician_gazebo](https://github.com/asanolab/robot_control/assets/6872136/aaff7d08-e705-4bf9-9fa3-c4e091bab148)
