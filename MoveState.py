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
        t.linear.x = 0.3

        left = self.GetMachine().GetVision().LeftImageCount()
        right = self.GetMachine().GetVision().RightImageCount()

        #check if an object is in view
        #print left
        #print right

        
        if left >= right:
            t.angular.z = 0.3
        else:#rot right
            t.angular.z = -0.3


        

        self.__pub.publish(t)       
        
    
    
    
    


