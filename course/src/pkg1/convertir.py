#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String, Float32,Int32

hour = 0

def time_callback(msg):
    global hour 
    hour = msg.data

def convertor():
    rospy.init_node('convertisseur')
    time_sub = rospy.Subscriber("/time",String,time_callback) 
    while(hour == 0):
        a = 1

    while not rospy.is_shutdown():
        real_time = time.ctime(float(hour))
        rospy.loginfo("Il est actuellement " + real_time)
        #rospy.spin()#empeche Python de fermer la node thant qu'on l'a pas stoppée


if __name__ == '__main__':
    try:
        convertor()
    except rospy.ROSInterruptException:
        print("End")
