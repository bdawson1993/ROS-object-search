#!/usr/bin/env python
class Transition(object):
    def __init__(self, stateName,transName ,stateMachine):
        self.__nextState = stateName
        self.__moveToNextState = False
        self.__stateMachine = stateMachine
        self.__transitionName = transName

    #get the name of the next state    
    def NextState(self):
        return self.__nextState
    
    
    def SetMoveToNextState(self,value):
        self.__moveToNextState = value        
    
    def MoveToNextState(self):
        return self.__moveToNextState
        
    def CheckTransition(self):
        raise NotImplementedError()
        
    def Reset(self):
        self.__moveToNextState = False
        
    def GetMachine(self):
        return self.__stateMachine

    def GetTransitionName(self):
        return self.__transitionName

    
        

