import rospy
from sensor_msgs.msg import LaserScan
from kobuki_msgs.msg import BumperEvent
from StateMachine import Transition
from StateMachine import MachineState

class Laser:
    def __init__(self):
        self.__laserSub = rospy.Subscriber("/scan", LaserScan, self.processScanData)
        self.__laserData = LaserScan()
        self.__scanThreshold = 5 #threshold of ranges

        #scan avgs - > 0.5 assume potential collision
        self.__frontScan = 100 #set to 100 to avoid false entries on startup
        self.__leftScan = 100
        self.__rightScan = 100
        

    def processScanData(self, data):
        self.__laserData = data

        #calculte scan data
        dataLen = len(data.ranges)
        self.__frontScan = sum(data.ranges[dataLen/2:dataLen/2 + self.__scanThreshold])/self.__scanThreshold
        self.__leftScan = sum(data.ranges[0:self.__scanThreshold])/self.__scanThreshold
        self.__rightScan = sum(data.ranges[dataLen - self.__scanThreshold:dataLen])/self.__scanThreshold

        print "Front Scan " + str(self.__frontScan)
        #print "Left Scan "  + str(self.__leftScan)
        #print "Right Scan "  + str(self.__rightScan)


    def GetLeft(self):
        return self.__leftScan

    def GetFront(self):
        return self.__frontScan

    def GetRight(self):
        return self.__rightScan
