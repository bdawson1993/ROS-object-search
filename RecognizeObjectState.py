from StateMachine import MachineState

class RecognizeObjectState(MachineState.MachineState):
    def __init__(self, machine, transistions):
        super(RecognizeObjectState, self).__init__("Recognize Object", machine, transistions)
        

    def Start(self):
        self.__values = self.GetMachine().GetVision().GetFind()

    def Update(self):
        count = (self.GetMachine().GetVision().GetImage() > 253).sum()
        
        #print values
        if count > 600:
            while True:
                #try and narrow down what object the robot is looking at
                if self.__values[0] == True:
                    self.GetMachine().GetVision().SetFind("BLUE", False)
                    count = (self.GetMachine().GetVision().GetImage() > 253).sum()
                    if count < 700:
                        print "Found Blue"
                        self.__values[0] = False
                        break
                        
                if self.__values[1] == True:
                    self.GetMachine().GetVision().SetFind("GREEN", False)
                    count = (self.GetMachine().GetVision().GetImage() > 253).sum()
                    if count < 700:
                        print "Found Green"
                        self.__values[1] = False
                        break

                if self.__values[2] == True:
                    self.GetMachine().GetVision().SetFind("RED", False)
                    count = (self.GetMachine().GetVision().GetImage() > 253).sum()
                    if count < 700:
                        print "Found Red"
                        self.__values[2] = False
                        break

                if self.__values[3] == True:
                    self.GetMachine().GetVision().SetFind("YELLOW", False)
                    count = (self.GetMachine().GetVision().GetImage() > 253).sum()
                    if count < 700:
                        print "Found Yellow"
                        self.__values[3] = False
                        break

        #set all values calculated back to vision
        self.GetMachine().GetVision().SetFind("BLUE", self.__values[0])
        self.GetMachine().GetVision().SetFind("GREEN", self.__values[1])
        self.GetMachine().GetVision().SetFind("RED", self.__values[2])
        self.GetMachine().GetVision().SetFind("YELLOW", self.__values[3])

        #force transition to set true
        self.Transitions()[0].SetMoveToNextState(True)


        

