#!/usr/bin/env python
import numpy
import rospy
import control


from StateMachine import StateMachine

import StartState
import StartTransition
import MoveState
import MoveTransition

import cv2

class Search:
    def __init__(self):
        rospy.init_node("vision", anonymous=True)
               
        #prepare state machine
        mach = StateMachine.StateMachine()
        
        #create start state
        startTrans = []
        startTrans.append(StartTransition.StartTransition(mach))        
        startState = StartState.StartState(mach,startTrans)
        
        #create move state
        moveTrans = []
        moveTrans.append(MoveTransition.MoveTransition(mach))
        moveState = MoveState.MoveState(mach, moveTrans)        
        
        #add mach state
        mach.AddState(startState)
        mach.AddState(moveState)
        
        
        #finish loading 
        mach.FinishLoading() 
        
        
        while not rospy.is_shutdown():
            
            mach.Update()
            #x = (v.GetImage() > 253).sum() #253 or greater
            
            
            #print x
            
        
        
                
        
        
                                          
                                         

s = Search()
    

    
    
