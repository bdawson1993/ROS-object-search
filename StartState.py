#!/usr/bin/env python
import MachineState as State

class StartState(State.MachineState):
    def __init__(self, stateName, transitions):
        State.MachineState.__stateName = stateName
        State.MachineState.__transitions = transitions
    
    def Start(self):
        print "Hello from start state"

