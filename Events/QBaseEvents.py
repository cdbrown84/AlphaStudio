from abc import abstractmethod, ABCMeta
from enum import Enum
from .QTypes import *


class QBaseEvents(object):
    __metaclass__ = ABCMeta


    def __init__(self):
        self.loggingEnabled = False


    def logEvent(self):
        
        if self.loggingEnabled == True:

            print("logging")
