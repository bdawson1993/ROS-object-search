#!/usr/bin/env python
from StateMachine import Transition
from StateMachine import MachineState

class MoveTransition(Transition.Transition):
    def __init__(self, stateMachine):
        Transition.Transition.__init__(self, "Move", stateMachine)
       
        
    def CheckTransition(self):
        print self.__stateMachine.__states[0].__stateName
