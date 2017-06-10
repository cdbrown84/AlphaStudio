import datetime
import os, os.path
import pandas as pd
from enum import Enum

from abc import ABCMeta, abstractmethod

class DataStatus(Enum):
    Active = 1
    Complete = 2

class DataManager(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):

        raise NotImplementedError("Method __init__() not implemented")

    @abstractmethod
    def getLatestBar(self, processed_data):

        raise NotImplementedError("method getLastestBar() not implemented")

    @abstractmethod
    def peekNextBar(self, quandlCode):

        raise NotImplementedError("method peekNextBar() not implemented")

    @abstractmethod
    def popNextBar(self, quandlCode):

        raise NotImplementedError("method popNextBar() not implemented")

    @abstractmethod
    def updateAllBars(self):

        raise NotImplementedError("method updateAllBars() not implemented")

    def getDataStatus(self):

        raise NotImplementedError("Method getDataStatus() not implemented")