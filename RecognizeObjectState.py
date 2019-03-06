from StateMachine import MachineState

class RecognizeObjectState(MachineState.MachineState):
    def __init__(self, machine, transistions):
        super(RecognizeObjectState, self).__init__("Recognize Object", machine, transistions)
        

    def Start(self):
        self.GetMachine().GetVision().SetFind("YELLOW", False)

    def Update(self):
        count = (self.GetMachine().GetVision().GetImage() > 253).sum()
        values = self.GetMachine().GetVision().GetFind()
        #print values
        self.Transitions()[0].SetMoveToNextState(True)