from .QBaseEvents import QBaseEvents
from .QTypes import *

class QBarEvent(QBaseEvents):
    def __init__(self, period, timeStamp, symbol, open, high, low, close, volume,
                 open_interest = None, settle = None, adj_close = None,
                 resolution=Resolution.Day):

        self.eventType = EventType.Bar
        self.resolution = resolution
        self.period = period
        self.timeStamp = timeStamp
        self.symbol = symbol
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.open_interest = open_interest
        self.settle = settle
        self.adj_close = adj_close


