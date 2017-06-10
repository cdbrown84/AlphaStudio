from enum import Enum

#Resolution = Enum('Resolution', 'Tick Second Minute Hour Day Week Month Year')

class Resolution(Enum):
    Tick = 1
    Second = 2
    Minute = 3
    Hour = 4
    Day = 5
    Week = 6
    Month = 7
    Year = 8

class EventType(Enum):
    Tick = 1
    Bar = 2
    Signal = 3
    Order = 4
    Fill = 5

class SignalType(Enum):
    Buy = 1
    Sell = 2
    Liquidate = 3

class OrderDirectionType(Enum):
    BuyToOpen = 1
    SellToOpen = 2
    BuyToClose = 3
    SellToClose = 4

class OrderType(Enum):
    MKT = 1
    LMT = 2
    STOPMKT = 3
    STOPLMT = 4