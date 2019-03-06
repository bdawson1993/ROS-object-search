from StateMachine import MachineState

class RecognizeObjectState(MachineState.MachineState):
    def __init__(self, machine, transistions):
        super(RecognizeObjectState, self).__init__("Recognize Object", machine, transistions)

    def Start(self):
        print "Start"

    def Update(self):
        count = (self.GetMachine().GetVision().GetImage() > 253).sum()
        self.GetMachine().GetVision().SetFind("YELLOW")