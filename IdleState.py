from StateMachine import MachineState
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class IdleState(MachineState.MachineState):

    def __init__(self,machine, transistions):
        super(IdleState, self).__init__("Idle", machine, transistions)

    def Start(self):
        self.__client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.__client.wait_for_server()
        
        ##move to start postion
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = 0
        goal.target_pose.pose.position.y = 0
        goal.target_pose.pose.orientation.w = 1.0
        self.__client.send_goal(goal)

    