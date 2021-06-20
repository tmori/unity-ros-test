#!/bin/bash

WORKSPACE_DIR=$(cd .. && pwd)

sudo docker run  \
	 -it --rm  --net host --name unity-ros-test unit-ros-test/hakoniwa:v1.0.0
