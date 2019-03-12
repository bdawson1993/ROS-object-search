#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from kobuki_msgs.msg import BumperEvent
from StateMachine import Transition
from StateMachine import MachineState

class OnBump(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnBump,self).__init__("Recognize Object", stateMachine)
        #self.__sub = rospy.Subscriber("/mobile_base/events/bumper",BumperEvent, self.processBumpData)
        self.__laserSub = rospy.Subscriber("/scan", LaserScan, self.processScanData)


        self.__bump = False

    def CheckTransition(self):
        if self.__bump == True:
            self.SetMoveToNextState(True)
            self.__bump = False
            

    def processScanData(self, data):
        dataLen = len(data.ranges)
        scanMean = sum(data.ranges[dataLen/2:dataLen/2 + 5])/5
        if scanMean < 0.5:
            self.SetMoveToNextState(True)

    def processBumpData(self, data):
        self.__bump = data.PRESSED

    
        