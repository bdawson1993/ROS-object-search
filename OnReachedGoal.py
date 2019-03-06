import rospy
from StateMachine import Transition
from actionlib_msgs.msg import GoalStatusArray

class OnReachedGoal(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnReachedGoal,self).__init__("Start", stateMachine)
        self.__sub = rospy.Subscriber("/mobile_base/events/bumper",GoalStatusArray, self.proccessGoalData)
        self.__bump = False

    def proccessGoalData(self, data):
        a = data[0]
        print a


    