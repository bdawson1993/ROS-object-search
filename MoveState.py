#!/usr/bin/env python
from StateMachine import MachineState

class MoveState(MachineState.MachineState):
    
    def __init__(self, machine, transistions):
        MachineState.MachineState.__init__(self,"Move", machine, transistions)

    def Start(self):
        print "Start"

    def Update(self):
        print "Update"        
        
    
    
    
    


