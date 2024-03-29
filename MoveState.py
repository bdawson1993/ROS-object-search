#!/usr/bin/env python
from StateMachine import MachineState
import rospy
from geometry_msgs.msg import Twist

class MoveState(MachineState.MachineState):
    
    def __init__(self, machine, transistions):
        super(MoveState, self).__init__("Move", machine, transistions)

    def Start(self):
        self.__pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 1)

    def Update(self):
        t = Twist()
        t.linear.x = 0.5

        left = self.GetMachine().GetVision().LeftImageCount()
        right = self.GetMachine().GetVision().RightImageCount()
        leftLaser = self.GetMachine().GetLaser().GetLeft()
        rightLaser = self.GetMachine().GetLaser().GetRight()

        potColl = (leftLaser <= 1.5)
        potColl = (rightLaser <= 1.5)

        #print leftLaser
        #print rightLaser 
        if potColl == False:
            #try to centre image
            if left >= right:
                t.angular.z = 0.3
            else:#rot right
                t.angular.z = -0.3
        else: #avoid pot collsions
            if leftLaser < 1.0:
                t.angular.z = 1.5
            if rightLaser < 1.0:
                t.angular.z = -1.5


        


    

        self.__pub.publish(t)     

    
        
    
    
    
    


