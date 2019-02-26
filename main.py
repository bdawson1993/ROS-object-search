#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from nav_msgs.msg import OccupancyGrid
import control
import vision


class Search:
    def __init__(self):
        rospy.init_node("vision", anonymous=True)
        c = control.Control()
        v = vision.Vision()
        rospy.spin()
                                          
                                         

s = Search()
    

    
    
