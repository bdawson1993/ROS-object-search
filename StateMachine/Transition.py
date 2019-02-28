#!/usr/bin/env python
class Transition:
    def __init__(self, stateName):
        self.__nextState = stateName
        self.__moveToNextState = False
          
    def NextState(self):
        return self.__nextState
        
    def MoveToNextState(self):
        return self.__moveToNextState
        
    def CheckTransition(self):
        raise NotImplementedError()
        
    def Reset(self):
        self.moveToNextState = False
        

