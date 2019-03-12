#!/usr/bin/env python
from StateMachine import Transition


class OnSeeObject(Transition.Transition):
    def __init__(self, stateMachine):
        #Transition.Transition.__init__(self,"Move", stateMachine)
        super(OnSeeObject, self).__init__("Move", "On See Object", stateMachine)
        
       
        
        
    def CheckTransition(self):
        if((self.GetMachine().GetVision().GetImage() > 253).sum() > 700):
            self.SetMoveToNextState(True)

        
        
        
        
       

