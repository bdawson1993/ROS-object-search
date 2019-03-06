import rospy
import numpy
from StateMachine import Transition
from actionlib_msgs.msg import GoalStatusArray

class OnReachedGoal(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnReachedGoal,self).__init__("Start", stateMachine)
        self.__sub = rospy.Subscriber("/move_base/status",GoalStatusArray, self.proccessGoalData)
        

    def CheckTransition(self):
        print "checking"


    def proccessGoalData(self, data):
       
        #GoalStatusArray.
        a = data._full_text
        print a
        


    