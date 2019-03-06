from StateMachine import MachineState

class RecognizeObjectState(MachineState.MachineState):
    def __init__(self, machine, transistions):
        super(RecognizeObjectState, self).__init__("Recognize Object", machine, transistions)
        self.__temp

    def Start(self):
        self.GetMachine().GetVision().SetFind("YELLOW")

    def Update(self):
        count = (self.GetMachine().GetVision().GetImage() > 253).sum()
        