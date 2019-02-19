#!/usr/bin/env python

import rospy
import numpy as np
from cv2 import namedWindow, cvtColor, imshow
from cv2 import destroyAllWindows, startWindowThread
from cv2 import COLOR_BGR2GRAY, waitKey
from cv2 import blur, Canny
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from nav_msgs.msg import OccupancyGrid




class RobotVision:

    def __init__(self):
        self.map = None
        self.bridge = CvBridge()
                                         
        self.image_sub = rospy.Subscriber(
             "/camera/rgb/image_raw",
            Image, self.callback)
            
        self.map_sub = rospy.Subscriber("/map", OccupancyGrid, self.showMap)

    def callback(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data)
        namedWindow("Robot Vision")
        imshow("Robot Vision",cv_image)
        waitKey(1)
        
    def showMap(self, data):
        image = self.bridge.numpy_type_to_cvtype(data.data.serialize_numpy)
        namedWindow("Map")
        imshow("Map", image)
        waitKey(1)
        
        
        
    

startWindowThread()
rospy.init_node('image_converter')
ic = RobotVision()
rospy.spin()

destroyAllWindows()
