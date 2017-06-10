from .QBaseEvents import QBaseEvents
from .QTypes import *



class QTickEvent(QBaseEvents):

    def __init__(self, timeStamp, symbol, bid, ask, bid_size=None, ask_size=None):

        self.eventType = EventType.Tick
        self.timeStamp = timeStamp
        self.symbol = symbol
        self.bid = bid
        self.ask = ask
        self.bid_size = bid_size
        self.ask_size = ask_size
