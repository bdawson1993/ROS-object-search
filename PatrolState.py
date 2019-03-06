from StateMachine import MachineState
import rospy
from geometry_msgs.msg import PoseStamped


class PatrolState(MachineState.MachineState):
    def __init__(self, machine, transistions):
        super(PatrolState, self).__init__("Patrol", machine, transistions)

    def Start(self):
        self.__pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)
        a = PoseStamped()
        a.header.stamp = "now"

    def Update(self):
        print "Patrolling..."
        
        
