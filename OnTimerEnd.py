#!/usr/bin/env python
import rospy
from StateMachine import Transition
from StateMachine import MachineState

class OnTimerEnd(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnTimerEnd,self).__init__("Patrol", stateMachine)
        self.__interval = 30
        self.__counter = 0

    def CheckTransition(self):
        if self.__counter <= self.__interval:
            self.SetMoveToNextState(True)
            self.__counter = 0
        else:
            self.__counter += 1

    