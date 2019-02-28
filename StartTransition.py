#!/usr/bin/env python
from StateMachine import Transition
from StateMachine import MachineState

class StartTransition(Transition.Transition):
    def __init__(self):
        Transition.Transition.__init__(self, "Start")
       
        
        
    def CheckTransition(self):
        print "Transition Check"

