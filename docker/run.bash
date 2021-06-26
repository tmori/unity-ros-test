#!/bin/bash

WORKSPACE_DIR=$(cd .. && pwd)


sudo docker run   \
	 -it --rm   -p 11311:11311 --ip=localhost:172.23.107.13 --name ros-test ros-test/hakoniwa:v1.0.0
