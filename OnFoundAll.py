from StateMachine import Transition

class OnFoundAll(Transition.Transition):
    def __init__(self, stateMachine):
        super(OnFoundAll,self).__init__("Idle", "On Found All", stateMachine)
        


    def CheckTransition(self):
        values = self.GetMachine().GetVision().GetFind()
        count = 0

        for i in range(0,3):
            if(values[i] == True):
                count+=1

        if count == 0:
            self.SetMoveToNextState(True)
            self.GetMachine().EndTime()





