#!/usr/bin/env python
import rospy
from kobuki_msgs.msg import BumperEvent
from StateMachine import Transition
from StateMachine import MachineState

class OnBumpTransition(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnBumpTransition,self).__init__("Recognize Object", stateMachine)
        self.__sub = rospy.Subscriber("/mobile_base/events/bumper",BumperEvent, self.processBumpData)
        self.__bump = False

    def CheckTransition(self):
        if self.__bump == True:
            self.SetMoveToNextState(True)

    def processBumpData(self, data):
        #BumperEvent.
        self.__bump = data.PRESSED

    
        