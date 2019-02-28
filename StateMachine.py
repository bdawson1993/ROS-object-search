#!/usr/bin/env python
import Transition
import MachineState

#Converion of my state machine library written in c# 

class StateMachine:
    
    def __init__(self):
        self.__states = list()
        self.__currentState = MachineState.MachineState()
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
        if(self.hasLoaded == True):
            self.__currentState.Update()
            self.__currentState.CheckTransistions()
            self.__CheckTransition()
     
    #perform tran checks on current state      
    def CheckTransition(self):
        for trans in self.currentState.Transitions():
            if trans.MoveToNextState() == True:
                stateName = trans.NextState()
                self.ChangeState(stateName)
                trans.Reset()
                
    #change state
    def ChangeState(self, stateName):
        for state in self.states:
            if(state.StateName() == stateName):
                self.currentState = state
                self.ChangeState.Start()
                break
        
        

                
        
