#!/usr/bin/env python

from StateMachine import Transition
from StateMachine import MachineState

class OnEmptyVisionTransition(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnEmptyVisionTransition,self).__init__("Start", stateMachine)
        
       
        
    def CheckTransition(self):
        total = (self.GetMachine().GetVision().GetImage() > 253).sum()

        print total
        if total == 0:
            self.SetMoveToNextState(True)
