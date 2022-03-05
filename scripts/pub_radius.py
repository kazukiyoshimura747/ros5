#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('pub_radius')
pub = rospy.Publisher('/radius', Int32, queue_size = 1)
rate = rospy.Rate(10)
r = 0
while not rospy.is_shutdown():
    r = int(input('input radius: '))
    pub.publish(r)
    rate.sleep()

