#!/usr/bin/env python
import Transition

class MachineState:
    def __init__(self, stateName, transitions):
        self.__stateName = stateName
        self.__transitions = transitions
        
    def __init__(self):
        self.__stateName = "DEFAULT"
        self.__transitions = list()
        
    #return statename to the state machine
    def StateName(self):
        return self.stateName
    
    #perform any startup actions
    def Start(self):
        raise NotImplementedError()
    
    #peform the update step of the state
    def Update(self):
        raise NotImplementedError()
        
    #perform all transistion checks
    def CheckTransistions(self):
        for i in self.transitions:
            i.CheckTransition()
     
    #return all transition to state machine        
    def Transitions(self):
        return self.transitions
            
        
        
        