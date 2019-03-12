#!/usr/bin/env python

from StateMachine import Transition
from StateMachine import MachineState

class OnEmptyVision(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnEmptyVision,self).__init__("Patrol","On Empty Vision", stateMachine)
        
       
        
    def CheckTransition(self):
        total = (self.GetMachine().GetVision().GetImage() > 253).sum()

       
        if total == 0:
            self.SetMoveToNextState(True)
