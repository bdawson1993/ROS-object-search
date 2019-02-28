#!/usr/bin/env python
class Transition:
    def __init__(self):
        self.nextState = str()
        self.moveToNextState = False
          
    def NextState(self):
        return self.nextState
        
    def MoveToNextState(self):
        return self.moveToNextState
        
    def CheckTransition(self):
        raise NotImplementedError()
        
    def Reset(self):
        self.moveToNextState = False
        

