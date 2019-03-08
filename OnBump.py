#!/usr/bin/env python
import rospy
from kobuki_msgs.msg import BumperEvent
from StateMachine import Transition
from StateMachine import MachineState

class OnBump(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnBump,self).__init__("Recognize Object", stateMachine)
        self.__sub = rospy.Subscriber("/mobile_base/events/bumper",BumperEvent, self.processBumpData)
        self.__bump = False

    def CheckTransition(self):
        if self.__bump == True:
            self.SetMoveToNextState(True)
            self.__bump = False
            

    def processBumpData(self, data):
        self.__bump = data.PRESSED

    
        