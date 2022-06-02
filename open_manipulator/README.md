# Install

```
cd ~/catkin_ws/src
wstool merge -t . robot_control/open_manipulator/install/open_manipulator.rosinstall
wstool update

rosdep install -y -r --from-paths . --ignore-src # execute on src dir
```
