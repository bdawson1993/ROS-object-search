from StateMachine import StateMachine
import vision
import laser

class SearchStateMachine(StateMachine.StateMachine):
    def __init__(self):
        super(SearchStateMachine, self).__init__()
        self.__vision = vision.Vision()
        self.__laser = laser.Laser()


    def GetVision(self):
        return self.__vision

    def GetLaser(self):
        return self.__laser