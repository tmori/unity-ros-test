#!/usr/bin/env python

import random
import rospy
from robotics_demo.msg import Actuator


TOPIC_NAME = 'actuator'
NODE_NAME = 'actuator_publisher'


def post_actuator():
    pub = rospy.Publisher(TOPIC_NAME, Actuator, queue_size=10)
    rospy.init_node(NODE_NAME, anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        topic_data = Actuator(0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4)
        pub.publish(topic_data)
        rate.sleep()


if __name__ == '__main__':
    try:
        post_actuator()
    except rospy.ROSInterruptException:
        pass
