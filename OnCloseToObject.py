#!/usr/bin/env python
import rospy
import numpy
from sensor_msgs.msg import LaserScan
from kobuki_msgs.msg import BumperEvent
from StateMachine import Transition
from StateMachine import MachineState

class OnCloseToObject(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnCloseToObject,self).__init__("Recognize Object", stateMachine)
        

    def CheckTransition(self):
        las = self.GetMachine().GetLaser()

        if las.GetFront() < 0.5:
            self.SetMoveToNextState(True)

    
        