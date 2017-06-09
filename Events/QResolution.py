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