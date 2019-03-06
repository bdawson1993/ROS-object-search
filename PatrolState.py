from StateMachine import MachineState
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal



class PatrolState(MachineState.MachineState):
    def __init__(self, machine, transistions):
        super(PatrolState, self).__init__("Patrol", machine, transistions)

    def Start(self):
        self.__client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.__client.wait_for_server()

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = 1.0
        goal.target_pose.pose.position.y = 1.0
        goal.target_pose.pose.orientation.w = 1.0
        self.__client.send_goal(goal)
        
        

        
        


    def Update(self):
        self.Transitions()[0].SetClient(self.__client)
        
        
