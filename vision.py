#!/usr/bin/env python

import rospy
import cv2 
import numpy

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class Vision:

    def __init__(self):
        
        #setup
        cv2.startWindowThread()
        self.__thresh_img = numpy.zeros(0)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",
                                         Image, self.processImage)
        
        #left and right image
        self.__leftImage = numpy.zeros(0)
        self.__rightImage = numpy.zeros(0)
        
        self.__findRed = True
        self.__findGreen = True
        self.__findBlue = True
        self.__findYellow = True
        
        
        
       
       #process image from the robot
    def processImage(self, data):
        cv2.namedWindow("Image window", 1)
        cv2.namedWindow("Thresh Window", 1)
        
        
        
       
        
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError, e:
            print e
        
        
        
        height = len(cv_image[:,1]  )
        width = len(cv_image[1,:]  )
        
         #define colors to be split
        yellowLow = numpy.array((0,101,101))
        yellowHigh = numpy.array((4,102,102))
        
        blueLow = numpy.array((101,0,0))
        blueHigh = numpy.array((255,0,0))
        
        
        redLow = numpy.array((0,0,101))        
        redHigh = numpy.array((4,4,255))
        
        greenLow = numpy.array((0,0,0))
        greenHigh = numpy.array((0,255,0))
        
        
        blue_thresh = numpy.zeros([width,height])
        yellow_thresh = numpy.zeros([width,height])
        red_thresh = numpy.zeros([width, height])        
        green_thresh = numpy.zeros([width, height])
        
        

        if self.__findBlue == True:        
        
            #thresh blue - good
            blue_thresh = cv2.inRange(cv_image,
                                     blueLow,
                                     blueHigh)
        
        if self.__findYellow == True:        
        
            #thresh yellow - good              
            yellow_thresh = cv2.inRange(cv_image,
                                     yellowLow,
                                     yellowHigh)
        
        if self.__findRed == True:        
        
            #thresh red - good                   
            red_thresh = cv2.inRange(cv_image,redLow,
                                     redHigh)
                                     
        if self.__findGreen == True:
            #green thresh
            green_thresh = cv2.inRange(cv_image, greenLow, 
                                       greenHigh)
                                 
        
        self.__thresh_img = blue_thresh + yellow_thresh + red_thresh + green_thresh
        self.__leftImage = self.__thresh_img[:,0:width/2]
        self.__rightImage = self.__thresh_img[:,width/2:width]
        
        
        #create grayscale and display images side by side
        grayScale = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
        numpy_hor = numpy.concatenate((grayScale, self.__thresh_img), axis=1)        
        
             
        cv2.imshow("Image window", numpy_hor)
        cv2.imshow("Thresh Window", green_thresh)
              
        
        cv2.waitKey(1)
        
        
        
        
        
    def __del__(self):
        cv2.destroyAllWindows()
        
    def GetImage(self):
        return self.__thresh_img
        
    def SetFind(self, value):
        if value == "BLUE":
            self.__findBlue = False
        if value == "Green":
            self.__findGreen = False
        if value == "RED":
            self.__findRed = False
        if value == "Yellow":
            self.__findYellow = False


