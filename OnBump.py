#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from StateMachine import Transition
from StateMachine import MachineState

class OnBump(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnBump,self).__init__("Recognize Object", stateMachine)
        #self.__sub = rospy.Subscriber("/mobile_base/events/bumper",BumperEvent, self.processBumpData)
        self.__laserSub = rospy.Subscriber("/scan", LaserScan, self.processScanData)


        self.__scanData = False

    def CheckTransition(self):
        if self.__scanData == True:
            self.SetMoveToNextState(True)
            self.__bump = False
            

    def processScanData(self, data):
        print data.ranges[525:555]

    
        