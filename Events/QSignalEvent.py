from .QBaseEvents import QBaseEvents
from .QTypes import *

class QSignalEvent(QBaseEvents):
    def __init__(self, timeStamp, symbol, last, signalType):
        self.eventType = EventType.Signal
        self.timeStamp = timeStamp
        self.symbol = symbol
        self.last = last
        self.signalType = signalType