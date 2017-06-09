from Q33Trader.BrokerConnections.IB.QClient import QClient
from Q33Trader.BrokerConnections.IB.QWrapper import QWrapper

class IBApp(QWrapper, QClient):
    def __init__(self):
        QWrapper.__init__(self)
        QClient.__init__(self, wrapper=self)