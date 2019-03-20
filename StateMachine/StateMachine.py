#!/usr/bin/env python
import MachineState
import vision
from time import sleep

#Converion of my state machine library written in c# 

class StateMachine(object):
    
    #init State machine with basic info
    def __init__(self):
        self.__states = list()
        self.__currentState = object()
        self.__hasLoaded = False
        self.__updateRate = 0.5
        self.__isNotClosed = True
        
      
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
            sleep(self.__updateRate)
     
    #perform tran checks on current state      
    def CheckTransition(self):
        for trans in self.__currentState.Transitions():
            if trans.MoveToNextState() == True:
                stateName = trans.NextState()
                self.ChangeState(stateName)
                trans.Reset() #reset trans 
                
    #change state
    def ChangeState(self, stateName):
        for state in self.__states:
            if(state.StateName() == stateName):
                nam = self.__currentState.StateName()
                self.__currentState.StateChange()
                self.__currentState = state
                self.__currentState.Start()
                print nam + " Changed to " + self.__currentState.StateName() + "\n"
                break #break when state has been found

    def GetCurrentState(self):
        return self.__currentState.StateName()

    def PrintInfo(self):
        print "State Machine: \n"
        print "Update Rate: " + str(self.__updateRate)

        for state in self.__states:
            print "State Name: " + state.StateName()
            print "Transitions:"
            for trans in state.Transitions():
                print " -------" + trans.GetTransitionName()
            print "\n"

    
    def Close(self):
        print "Closing Machine...Goodbye"
        self.__isNotClosed = False
        self.__hasLoaded = False



    def IsNotClosed(self):
        return self.__isNotClosed
                
        
        

                
        
