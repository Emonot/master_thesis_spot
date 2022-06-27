#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
import rosservice
import tf
import time

def callback(data):
    
    try:
        talker(data)
    except rospy.ROSInterruptException:
        pass

def talker(data):
    imuPub = rospy.Publisher('spot_imu', Imu, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    rospy.loginfo(data)
    imuPub.publish(data)

if __name__ == '__main__':
    rospy.init_node('spot_imu', anonymous=True)

    rospy.Subscriber("/imu/data", Imu, callback1)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()