from abc import abstractmethod, ABCMeta
from enum import Enum

EventType = Enum("EventType", "TICK BAR SIGNAL ORDER FILL")

class QBaseEvents(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass