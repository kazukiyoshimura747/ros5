#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def cb(message):
    print('Area of a circle with a radius of {0}cm = {1}cm*2' .format(message.data,message.data*message.data*3.14))

if __name__ == '__main__':
    rospy.init_node('sub_area')
    sub = rospy.Subscriber('/radius', Int32, cb)
    rospy.spin()
