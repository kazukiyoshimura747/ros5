#!/usr/bin/env python3

#// SPDX-License-Identifier: GPL-2.0
#/*
# *Copyright (C) 2022 Kazuki Yoshimura All rights reserved
# */

import rospy
from std_msgs.msg import Int32

def cb(message):
    print('Circumference of a circle with a radius of {0}cm = {1}cm' .format(message.data,message.data*2*3.14))

if __name__ == '__main__':
    rospy.init_node('sub_circumference')
    sub = rospy.Subscriber('/radius', Int32, cb)
    rospy.spin()

