# swiftpro_interface
Software for uArm SwiftPro
- References
  - API (github)
    - https://github.com/uArm-Developer/RosForSwiftAndSwiftPro

## Setup & build
Setup workspace
- https://github.com/asanolab/robot_control

Build
```bash
cd swiftpro_interface
catkin bt
```

### Robot hardware setup
- Turn on the power button (orange)
- Connect the robot to your computer by USB cable
- Add permission to the robot device 
   ```
   sudo chmod 666 /dev/ttyACM0
   ```
   or add permission permanently
   ```
   sudo usermod -a -G dialout $USER
   ```

## Visualization (Rviz)
- Just see the robot in Rviz
```
roslaunch swiftpro_interface swiftpro_display.launch
```
![swiftpro_rviz](https://github.com/asanolab/robot_control/assets/6872136/b7330b9b-67e6-4da3-8f43-22b92f66f00f)


## Manipulation (moveit)
### Test motion through script program
```
roslaunch swiftpro_interface swiftpro_moveit_manip.launch
rosrun swiftpro_interface test_manip_swiftpro.py
```
![swiftpro_moveit](https://github.com/asanolab/robot_control/assets/6872136/b9810777-de69-430a-a857-f341f8551f21)

### Interactive motion
- use moveit to move the robot interactively
```
roslaunch pro_moveit_config demo.launch
```


## Pump
```
roslaunch swiftpro_interface swiftpro_bringup.launch

cd scripts
./test_pump_on.py   # pump on
./test_pump_off.py  # pump off
```
