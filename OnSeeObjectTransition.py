#!/usr/bin/env python
from StateMachine import Transition


class OnSeeObjectTransition(Transition.Transition):
    def __init__(self, stateMachine):
        #Transition.Transition.__init__(self,"Move", stateMachine)
        super(OnSeeObjectTransition, self).__init__("Move", stateMachine)
        
       
        
        
    def CheckTransition(self):
        if((self.GetMachine().GetVision().GetImage() > 253).sum() > 100):
            self.SetMoveToNextState(True)
        
        
        
       

