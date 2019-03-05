from StateMachine import StateMachine
import vision

class SearchStateMachine(StateMachine.StateMachine):
    def __init__(self):
        super(SearchStateMachine, self).__init__()
        self.__vision = vision.Vision()


    def GetVision(self):
        return self.__vision