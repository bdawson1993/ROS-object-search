#!/usr/bin/env python
from StateMachine import MachineState
import rospy
from geometry_msgs.msg import Twist

class MoveState(MachineState.MachineState):
    
    def __init__(self, machine, transistions):
        super(MoveState, self).__init__("Move", machine, transistions)

    def Start(self):
        self.__pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 2)

    def Update(self):
        t = Twist()
        t.linear.x = 0.1

        self.__pub.publish(t)       
        
    
    
    
    


