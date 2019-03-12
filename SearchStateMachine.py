from StateMachine import StateMachine
import vision
import laser

class SearchStateMachine(StateMachine.StateMachine):
    def __init__(self):
        super(SearchStateMachine, self).__init__()
        self.__vision = vision.Vision()
        self.__laser = laser.Laser()
        self.__objectLoc = []


    def GetVision(self):
        return self.__vision

    def GetLaser(self):
        return self.__laser

    def AddLoc(self, name, x,y):
        ob = ObjectLoc()
        ob.SetLoc(name,x, y)
        self.__objectLoc.append(ob)

class ObjectLoc:
    def __init__(self):
        self.__name = str()
        self.__x = 0
        self.__y = 0

    def SetLoc(self, name,x,y):
        print name + str(x) + str(y)
        self.__name = name
        self.__x = x
        self.__y = y