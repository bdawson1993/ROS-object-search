#!/usr/bin/env python
import MachineState
from time import sleep

#Converion of my state machine library written in c# 

class StateMachine:
    
    #init State machine with basic info
    def __init__(self):
        self.__states = list()
        self.__currentState = object() 
        self.__hasLoaded = False
        
      
     #add state to state machine
    def AddState(self, machineState):
        self.__states.append(machineState)
        
    #finish loading state machine and set current state to start processing
    def FinishLoading(self):
        self.__hasLoaded = True
        self.__currentState = self.__states[0]
        self.__currentState.Start()
    
    #perform update logic on current machine state
    def Update(self):
        if(self.__hasLoaded == True):
            self.__currentState.Update()
            self.__currentState.CheckTransistions()
            self.CheckTransition()
            sleep(0.5)
     
    #perform tran checks on current state      
    def CheckTransition(self):
        for trans in self.__currentState.Transitions():
            if trans.MoveToNextState() == True:
                stateName = trans.NextState()
                self.ChangeState(stateName)
                trans.Reset() #reset trans 
                
    #change state
    def ChangeState(self, stateName):
        for state in self.states:
            if(state.StateName() == stateName):
                self.currentState = state
                self.ChangeState.Start()
                break #break when state has been found
        
        

                
        
