#!/usr/bin/env python
import rospy
import numpy
from kobuki_msgs.msg import BumperEvent
from StateMachine import Transition
from StateMachine import MachineState
from geometry_msgs.msg import Twist

class OnBump(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnBump,self).__init__("Start","On Bump", stateMachine)
        self.__onBump = False
        self.__sub = rospy.Subscriber("/mobile_base/events/bumper", BumperEvent, self.processBump)
        self.__pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 1)
        

    def CheckTransition(self):
        if self.__onBump == True:
            self.SetMoveToNextState(True)
            self.__onBump = False #reset bump
            t = Twist()
            t.linear.x = -0.5
            self.__pub.publish(t)

    def processBump(self, data):
        self.__onBump = data.PRESSED