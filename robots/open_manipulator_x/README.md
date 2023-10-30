# Install

```
cd ~/catkin_ws/src
wstool merge -t . robot_control/open_manipulator/install/open_manipulator.rosinstall
wstool update

rosdep install -y -r --from-paths . --ignore-src # execute on src dir
catkin build
```

## for kinetic devel
In kinetic devel, open_manipulator.urdf.xacro is existing, but open_manipulator_robot.urdf.xacro is not.

```
roscd open_manipulator_description/urdf
cp open_manipulator.urdf.xacro open_manipulator_robot.urdf.xacro
```

# Sample
terminal1
```
roslaunch open_manipulator_controllers joint_trajectory_controller.launch sim:=false usb_port:=/dev/ttyACM0 
```

terminal2
```
./open_manipulator_x_sample.py
```
