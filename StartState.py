#!/usr/bin/env python
from StateMachine import MachineState
import rospy
from geometry_msgs.msg import Twist


class StartState(MachineState.MachineState):
    def __init__(self, mach, transitions):
        super(StartState, self).__init__("Start",mach, transitions)
        
        
    
    def Start(self):
        self.pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 2)
        
    def Update(self):
        t = Twist()
        t.angular.z = 0.8
        self.pub.publish(t)
        
    

