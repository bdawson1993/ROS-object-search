from StateMachine import MachineState
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import geometry_msgs

class RecognizeObjectState(MachineState.MachineState):
    def __init__(self, machine, transistions):
        super(RecognizeObjectState, self).__init__("Recognize Object", machine, transistions)
        #self.__odom = rospy.Subscriber("/odom", Pose, self.proccessOdom)
        self.__x = 0.0
        self.__y = 0.0

    def Start(self):
        self.__values = self.GetMachine().GetVision().GetFind()
        self.__threshold = 20000

    def Update(self):
        count = (self.GetMachine().GetVision().GetImage() > 253).sum()
        
        print count
        if count > 5000:
            while True:
                #try and narrow down what object the robot is looking at
                if self.__values[0] == True: #check blue
                    self.GetMachine().GetVision().SetFind("BLUE", False)
                    count = (self.GetMachine().GetVision().GetImage() > 253).sum()
                    if count < self.__threshold:
                        print "Found Blue"
                        #self.__values[0] = False
                        #self.GetMachine().AddLoc("Blue", self.__x, self.__y)
                        break
                    else:
                        self.GetMachine().GetVision().SetFind("BLUE", True)
                        
                if self.__values[1] == True: #check green
                    self.GetMachine().GetVision().SetFind("GREEN", False)
                    count = (self.GetMachine().GetVision().GetImage() > 253).sum()
                    if count < self.__threshold:
                        print "Found Green"
                        #self.__values[1] = False
                        break
                    else:
                        self.GetMachine().GetVision().SetFind("GREEN", True)


                if self.__values[2] == True: #check red
                    self.GetMachine().GetVision().SetFind("RED", False)
                    count = (self.GetMachine().GetVision().GetImage() > 253).sum()
                    if count < self.__threshold:
                        print "Found Red"
                        #self.__values[2] = False
                        break
                    else:
                        self.GetMachine().GetVision().SetFind("RED", True)

                if self.__values[3] == True: #check yellow
                    self.GetMachine().GetVision().SetFind("YELLOW", False)
                    count = (self.GetMachine().GetVision().GetImage() > 253).sum()
                    if count < self.__threshold:
                        print "Found Yellow"
                        #self.__values[3] = False
                        break
                    else:
                        self.GetMachine().GetVision().SetFind("YELLOW", True)

        #set all values calculated back to vision
        #self.GetMachine().GetVision().SetFind("BLUE", self.__values[0])
        #self.GetMachine().GetVision().SetFind("GREEN", self.__values[1])
        #self.GetMachine().GetVision().SetFind("RED", self.__values[2])
        #self.GetMachine().GetVision().SetFind("YELLOW", self.__values[3])

        #force transition to set true
        self.Transitions()[0].SetMoveToNextState(True)

    def StateChange(self):
        pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 2)
        t = Twist()
        t.linear.x = -0.5
        pub.publish(t)

    def proccessOdom(self, data):
        self.__x = data.x
        self.__y = data.y
        print self.__x


        

