#!/usr/bin/env python

import rospy
import vision 

class control:
    def __init__(self):
        vis = vision.Vision()
        
        self.image = vis.thresh_img
        
        
        

c = control()

