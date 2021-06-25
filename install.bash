#!/bin/bash


mkdir catkin_ws
mkdir catkin_ws/src

cp -rp unity/ROS-TCP-Endpoint catkin_ws/src/
echo "ROS_TCP_PORT: 10000" >> catkin_ws/src/ROS-TCP-Endpoint/config/params.yaml
cp -rp unity/Unity-Robotics-Hub/tutorials/ros_packages/robotics_demo catkin_ws/src/ 

cd catkin_ws
catkin_make
