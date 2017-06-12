from ..Utilities import QStrategy

class ExampleStrategy(QStrategy.QStrategy):

    def initialization(self):
        pass


    def onTick(self, qTick):
        pass


    def onBar(self, qBar):

        #Test
        print(qBar.close)


    def scheduler(self):
        pass


    def onOrder(self, qOrder):
        pass


    def execute(self):
        pass