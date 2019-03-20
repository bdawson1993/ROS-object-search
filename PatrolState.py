from StateMachine import MachineState
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal



class PatrolState(MachineState.MachineState):
    def __init__(self, machine, transistions):
        super(PatrolState, self).__init__("Patrol", machine, transistions)

        self.__routeX = [0.0, 0.0, 1.0, -4.0, -4.0]
        self.__routeY = [0.0, 4.0, -4.5,-0.3, 3.0]
        self.__currentNode = 0
        


    def Start(self):
        self.__client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        self.__client.wait_for_server()

        #move to current node on route
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = self.__routeX[self.__currentNode]
        goal.target_pose.pose.position.y = self.__routeY[self.__currentNode]
        goal.target_pose.pose.orientation.w = 1.0
        self.__client.send_goal(goal)
    
        

        self.Transitions()[0].SetClient(self.__client)
        
        
        

    def Update(self):
        if self.__client.get_state() == 3:
            self.__client.cancel_all_goals()



    def StateChange(self):
        if self.__client.get_state() == 3:
            if self.__currentNode < len(self.__routeX) - 1:
                self.__currentNode += 1
            else:
                self.__currentNode = 0
        
        self.__client.cancel_all_goals()

    def __del__(self):
        self.__client.cancel_all_goals()

        
        
        
