#!/usr/bin/env python
import numpy
import rospy
import control


from SearchStateMachine import SearchStateMachine

import StartState
import OnSeeObjectTransition
import MoveState
import OnBumpTransition

import cv2

class Search:
    def __init__(self):
        rospy.init_node("vision", anonymous=True)
               
        #prepare state machine
        mach = SearchStateMachine()
        
        #create start state
        startTrans = []
        startTrans.append(OnSeeObjectTransition.OnSeeObjectTransition(mach))        
        startState = StartState.StartState(mach,startTrans)
        
        #create move state
        moveTrans = []
        moveTrans.append(OnBumpTransition.OnBumpTransition(mach))
        moveState = MoveState.MoveState(mach, moveTrans)        
        
        #add mach state
        mach.AddState(startState)
        mach.AddState(moveState)
        
        
        #finish loading 
        mach.FinishLoading() 
        
        
        while not rospy.is_shutdown():
            
            mach.Update()
            
            
        
        
                
        
        
                                          
                                         

s = Search()
    

    
    
