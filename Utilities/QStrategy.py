from abc import abstractmethod, ABCMeta

class QStrategy(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.Bar = None
        self.Tick = None
        self.Order = None
        self.Signal = None
        self.Schedule = None
        self.initialization()


    @abstractmethod
    def initialization(self):

        raise NotImplementedError("Should implement initialization()")

    @abstractmethod
    def onTick(self, qTick):
        raise NotImplementedError("Should implement onTick()")

    @abstractmethod
    def onBar(self, qBar):

        raise NotImplementedError("Should implement onBar()")

    @abstractmethod
    def scheduler(self):
        raise NotImplementedError("Should implement scheduler()")

    @abstractmethod
    def onOrder(self, qOrder):

        raise NotImplementedError("Should implement onOrder()")

    @abstractmethod
    def execute(self):
        raise NotImplementedError("Should implement onOrder()")

    def runBackTest(self):
        pass

    def runSimulation(self):
        pass

    def runLiveStrategy(self):
        pass
