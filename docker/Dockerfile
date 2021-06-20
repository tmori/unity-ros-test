FROM ubuntu:18.04 as unity-ros-test

ARG DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-c"]

#install ros
RUN apt-get update && apt-get install -y \
	vim \
	curl \
	lsb-release \
	git 
RUN apt-get update \
	&& apt-get install -my wget gnupg

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' \
	&& curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - 


RUN apt update \
	&& apt-get install -y ros-melodic-desktop-full

RUN echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc \
	&& source /root/.bashrc 

RUN mkdir ~/workspace
WORKDIR /root/workspace
RUN git clone https://github.com/Unity-Technologies/Unity-Robotics-Hub.git \
	&& git clone https://github.com/Unity-Technologies/ROS-TCP-Endpoint.git

RUN mkdir -p catkin_ws/src
WORKDIR /root/workspace/catkin_ws

RUN cp -rp /root/workspace/ROS-TCP-Endpoint src/
RUN cp -rp /root/workspace/Unity-Robotics-Hub/tutorials/ros_packages/robotics_demo src/ 
RUN /bin/bash -c "source /opt/ros/melodic/setup.bash; catkin_make" \
	&& source devel/setup.bash 
