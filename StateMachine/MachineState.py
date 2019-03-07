#!/usr/bin/env python
import Transition
import StateMachine

class MachineState(object):
    def __init__(self):
        self.__stateName = "DEFAULT"
        self.__transitions = list()
        self.__stateMachine = StateMachine.StateMachine()
        
        
    def __init__(self, stateName, machine, transitions):
        self.__stateName = stateName
        self.__transitions = transitions
        self.__stateMachine = machine
        
    #return statename to the state machine
    def StateName(self):
        return self.__stateName
    
    #perform any startup actions
    def Start(self):
        raise NotImplementedError()
    
    #peform the update step of the state
    def Update(self):
        raise NotImplementedError()
        
    #cleanup state before change
    def StateChange(self):
        print "State Changed "
        
    #perform all transistion checks
    def CheckTransistions(self):
        for i in self.__transitions:            
            i.CheckTransition()
            
     
    #return all transition to state machine        
    def Transitions(self):
        return self.__transitions

    def GetMachine(self):
        return self.__stateMachine
            
        
        
        