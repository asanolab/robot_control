# Install

```
cd ~/catkin_ws/src/robot_control/open_manipulator
wstool merge -t . install/open_manipulator.rosinstall
wstool update

rosdep install -y -r --from-paths . --ignore-src # execute on src dir
```
