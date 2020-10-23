#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String, Float64, Int32

def timer():
    rospy.init_node("timer")
    timer_pub = rospy.Publisher("/time",String, queue_size=10)
    rate = rospy.Rate(10)


    while not rospy.is_shutdown():
        heure = str(rospy.get_rostime().secs)
        timer_pub.publish(heure)
        rate.sleep()


if __name__ == '__main__':
    try:
        timer()
    except rospy.ROSInterruptException:
        print("End")


            