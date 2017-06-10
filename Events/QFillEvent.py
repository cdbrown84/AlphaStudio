from .QBaseEvents import QBaseEvents
from .QTypes import *

class QFillEvent(QBaseEvents):
    def __init__(self, timeStamp, symbol, quantity, orderType,
                 orderDirectionType, fillPrice, commissions=None):

        self.timeStamp = timeStamp
        self.symbol = symbol
        self.quantity = quantity
        self.orderType = orderType
        self.orderDirectionType = orderDirectionType
        self.fillPrice = fillPrice
        self.commissions = commissions
        self.EventType = EventType.Fill



    def fillMessage(self, message):
        print(message)