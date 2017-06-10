from .QBaseEvents import QBaseEvents
from .QTypes import *

class QOrderEvent(QBaseEvents):
    def __init__(self, timeStamp, symbol, orderType, orderDirectionType, quantity):
        self.eventType = EventType.Order
        self.symbol = symbol
        self.timeStamp = timeStamp
        self.orderType = orderType
        self.orderDirectionType = orderDirectionType
        self.quantity = quantity

    def orderMessage(self):
        print("Order Submitted: Symbol=%s, Type=%s, , Direction=%s, Quantity=%s" % \
        (self.symbol, self.orderType, self.orderDirectionType, self.quantity))
