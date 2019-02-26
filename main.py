#!/usr/bin/env python

import rospy
import cv2
import numpy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class vision:

    def __init__(self):

        cv2.startWindowThread()
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",
                                          Image, self.callback)
        self.pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 2)
       

    def callback(self, data):
        cv2.namedWindow("Image window", 2)
        cv2.namedWindow("Image thresh", 1)
        
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError, e:
            print e


        yellow = numpy.array((0,102,102))
        blue = numpy.array((102,0,0))
        red = numpy.array((0,0,102))
        
        #thresh blue
        blue_thresh = cv2.inRange(cv_image,
                                 numpy.array((0, 0, 0)),
                                 blue)
        
        #thresh yellow                    
        yellow_thresh = cv2.inRange(cv_image,
                                 numpy.array((0, 0, 0)),
                                 yellow)
                                 
        red_thresh = cv2.inRange(cv_image,numpy.array((0,0,0)),
                                 red)
                                 
        thresh_img = blue_thresh + yellow_thresh + red_thresh
        
        
        
        
              
        
        t = Twist()
        t.angular.z = 1
        
        
        self.pub.publish(t)
        
        
        cv2.imshow("Image window", cv_image, thresh_img)
        cv2.imshow("Image window", thresh_img)
        
        cv2.waitKey(1)


vision()
rospy.init_node('image_converter', anonymous=True)
rospy.spin()
cv2.destroyAllWindows()