#!/usr/bin/env python
import numpy
import rospy
import control
import vision
from StateMachine import StateMachine
import StartState
import StartTransition
import cv2

class Search:
    def __init__(self):
        rospy.init_node("vision", anonymous=True)
        c = control.Control()
        v = vision.Vision()
        
        trans = []
        startTrans = StartTransition.StartTransition()
        trans.append(startTrans)        
        startState = StartState.StartState("start", trans)
        
        #prepare state machine
        mach = StateMachine.StateMachine()
        mach.AddState(startState)
        
        #finish loading 
        mach.FinishLoading() 
        
        
        while not rospy.is_shutdown():
            
            mach.Update()
            x = (v.GetImage() > 253).sum() #253 or greater
            
            
            print x
            
        
        
                
        
        
                                          
                                         

s = Search()
    

    
    
