#!/usr/bin/env python
import rospy
import numpy
from kobuki_msgs.msg import BumperEvent
from StateMachine import Transition
from StateMachine import MachineState

class OnBump(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnBump,self).__init__("Start","On Bump", stateMachine)
        self.__onBump = False
        self.__sub = rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, self.processBump)
        

    def CheckTransition(self):
        if self.__onBump == True:
            self.SetMoveToNextState(True)
            self.__onBump = False

    def processBump(self, data):
        self.__onBump = data.PRESSED