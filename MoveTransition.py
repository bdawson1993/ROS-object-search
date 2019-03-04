#!/usr/bin/env python
from StateMachine import Transition
from StateMachine import MachineState

class MoveTransition(Transition.Transition):
    def __init__(self, stateMachine):
        super(MoveTransition,self).__init__("Move", stateMachine)
       
        
    def CheckTransition(self):
        print "Moving"
