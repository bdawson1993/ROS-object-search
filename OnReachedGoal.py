import rospy
import numpy
from StateMachine import Transition
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class OnReachedGoal(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnReachedGoal,self).__init__("Start", stateMachine)
        
        

    def CheckTransition(self):
        if self.__client.get_state() == 3:
            print "Change"
            self.SetMoveToNextState(True)
        
    def SetClient(self, client):
        self.__client = client
        


    