#!/usr/bin/env python
from StateMachine import MachineState

class MoveState(MachineState.MachineState):
    
    def __init__(self, machine, transistions):
        super(MoveState, self).__init__("Move", machine, transistions)

    def Start(self):
        print "Start"

    def Update(self):
        print "Update"        
        
    
    
    
    


