#!/usr/bin/env python
import numpy
import rospy



from SearchStateMachine import SearchStateMachine
from std_msgs.msg import String

import StartState
import PatrolState
import MoveState
import RecognizeObjectState

import OnTimerEnd
import OnReachedGoal
import OnEmptyVisionTransition
import OnBumpTransition
import OnSeeObjectTransition

import cv2

class Search:
    def __init__(self):
        rospy.init_node("find", anonymous=True)
               
        #prepare state machine
        mach = SearchStateMachine()
        
        #create start state
        startTrans = []
        startTrans.append(OnSeeObjectTransition.OnSeeObjectTransition(mach)) 
        startTrans.append(OnTimerEnd.OnTimerEnd(mach))      
        startState = StartState.StartState(mach,startTrans)
        
        #create move state
        moveTrans = []
        moveTrans.append(OnEmptyVisionTransition.OnEmptyVisionTransition(mach))
        moveTrans.append(OnBumpTransition.OnBumpTransition(mach))
        moveState = MoveState.MoveState(mach, moveTrans)        
        
        #create reg state
        regTrans = []
        regTrans.append(OnEmptyVisionTransition.OnEmptyVisionTransition(mach))
        regState = RecognizeObjectState.RecognizeObjectState(mach, regTrans)
        
        #create patrol state
        patrolTrans = []
        patrolTrans.append(OnReachedGoal.OnReachedGoal(mach))
        patrolState = PatrolState.PatrolState(mach, patrolTrans)

        #add mach state
        mach.AddState(startState)
        mach.AddState(moveState)
        mach.AddState(regState)
        mach.AddState(patrolState)
        
        
        #finish loading 
        mach.FinishLoading() 
        self.__pub = rospy.Publisher("find", String, queue_size=1)
        
        while not rospy.is_shutdown():
            self.__pub.publish("State Machine: " + "State Name: " + mach.GetCurrentState())
            mach.Update()
            
            
        
        
                
        
        
if __name__ == "__main__":
    s = Search()
    

    
    
