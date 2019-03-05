#!/usr/bin/env python

from StateMachine import Transition
from StateMachine import MachineState

class OnBumpTransition(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnBumpTransition,self).__init__("Move", stateMachine)
        
       
        
    def CheckTransition(self):
        #print "Moving"
        x = 10
