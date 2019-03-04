#!/usr/bin/env python
from StateMachine import Transition


class StartTransition(Transition.Transition):
    def __init__(self, stateMachine):
        Transition.Transition.__init__(self,"Move", stateMachine)
        
       
        
        
    def CheckTransition(self):
        if((self.GetMachine().GetVision().GetImage() > 253).sum() > 20000):
            self.SetMoveToNextState(True)
        
        
        print (self.GetMachine().GetVision().GetImage() > 253).sum()
        
       

