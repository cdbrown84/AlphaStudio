from Q33Trader.DataManager import DataManager
from Q33Trader.Settings import Config
import quandl
import datetime

from datetime import date

class QuandlDataHandler(DataManager.DataManager):

    def __init__(self, start_date='2015-01-01', end_date='2016-01-01'):
        self.quandlAPI = Config.QuandlAPICode
        self.start_date = start_date
        self.end_date = end_date
        self.processed_data = {}
        self.dataStatus = DataManager.DataStatus.Active


    def getQuandlData(self, quandlCode):


        return quandl.get(quandlCode, authtoken=self.quandlAPI, start_date=self.start_date, end_date=self.end_date)

    '''
        Specifically formatted for Futures Data from CHRIS/CME
    '''

    def getFuturesDataType1(self, quandlCode):


        self.processed_data[quandlCode] = self.getQuandlData(quandlCode)

        self.processed_data[quandlCode].drop({'Settle', 'Change'}, axis=1, inplace=True)
        self.processed_data[quandlCode].rename(columns={'Open': quandlCode + '_Open', 'High': quandlCode + '_High', 'Low': quandlCode + '_Low',
                                       'Last': quandlCode + '_Last', 'Volume': quandlCode + '_Volume',
                                       'Previous Day Open Interest': quandlCode + '_Open_Interest'}, inplace=True)

    '''
        Specifically formatted for Stocks data from WIKI database
    '''
    def getStocksDataType1(self, quandlCode):
        self.processed_data[quandlCode] = self.getQuandlData(quandlCode)
        self.processed_data[quandlCode].drop({'Open', 'High', 'Low', 'Close', 'Volume', 'Ex-Dividend', 'Split Ratio'}, axis=1,
                            inplace=True)
        self.processed_data[quandlCode].rename(
            columns={'Adj. Open': quandlCode + '_Open', 'Adj. High': quandlCode + '_High', 'Adj. Low': quandlCode + '_Low',
                     'Adj. Close': quandlCode + '_Last', 'Adj. Volume': quandlCode + '_Volume',
                     }, inplace=True)


    '''
        Specifically formatted for ETFs from WIKI database
    '''
    def getEftsDataType1(self, quandlCode):
        self.processed_data[quandlCode] = self.getQuandl(quandlCode)
        self.processed_data[quandlCode].rename(columns={'Open': quandlCode + '_Open', 'High': quandlCode + '_High', 'Low': quandlCode + '_Low',
                                       'Close': quandlCode + '_Last', 'Volume': quandlCode + '_Volume',
                                       }, inplace=True)
    '''
        Method will get the latest bar for a given symbol
    '''
    def getLatestBar(self, quandlCode):

        activeData = self.processed_data[quandlCode]

        try:
            if len(self.processed_data[quandlCode] > 1):
                self.dataStatus = DataManager.DataStatus.Active
                currentBar = (
                ([quandlCode, activeData.index[0], float(activeData[quandlCode + '_Open'][0]), float(activeData[quandlCode + '_High'][0]),
                  float(activeData[quandlCode + '_Low'][0]),
                  float(activeData[quandlCode + '_Last'][0]), activeData[quandlCode + '_Volume'][0]])
                )
                return currentBar
            else:
                self.dataStatus = DataManager.DataStatus.Complete
                return self.dataStatus
        except IndexError:
            self.dataStatus = DataManager.DataStatus.Complete

    '''
        Method will look at the next bar but not remove it from the dataframe for a given symbol
    '''
    def peekNextBar(self, quandlCode):

        try:

            if len(self.processed_data[quandlCode] >1):
                self.dataStatus = DataManager.DataStatus.Active
                activeData = self.processed_data[quandlCode]
                nextBar = (([quandlCode, activeData.index[0], float(activeData[quandlCode + '_Open'][1]), float(activeData[quandlCode + '_High'][1]),
                   float(activeData[quandlCode + '_Low'][1]),
                   float(activeData[quandlCode + '_Last'][1]), activeData[quandlCode + '_Volume'][1]]))
                return nextBar
            else:
                self.dataStatus = DataManager.DataStatus.Complete
                return None
        except IndexError:
            self.dataStatus = DataManager.DataStatus.Complete
            return None

    '''
        Method will remove the current bar from the dataframe for a given symbol
    '''
    def popNextBar(self, quandlCode):

        try:

            if len(self.processed_data[quandlCode]) > 1:

                self.dataStatus = DataManager.DataStatus.Active
                activeData = self.processed_data[quandlCode][1:]
                self.processed_data[quandlCode] = activeData
            else:
                self.dataStatus = DataManager.DataStatus.Complete
        except IndexError:
            self.dataStatus = DataManager.DataStatus.Complete

    '''
        Update all Bars for all symbols. This will remove the current bar for each symbol
    '''
    def updateAllBars(self):
        try:

            for key in self.processed_data:
                self.popNextBar(key)
        except IndexError:

            self.dataStatus = DataManager.DataStatus.Complete

    def getDataStatus(self):
        return self.dataStatus

# Testing



test = QuandlDataHandler(start_date='2010-01-01')
test.getFuturesDataType1('CHRIS/CME_ES1')
test.getFuturesDataType1('CHRIS/CME_CL1')
test.getFuturesDataType1('CHRIS/CME_GC1')
while test.dataStatus == DataManager.DataStatus.Active:


    print(test.getLatestBar('CHRIS/CME_ES1'))
    print(test.peekNextBar('CHRIS/CME_ES1'))
    print(test.getLatestBar('CHRIS/CME_CL1'))
    print(test.peekNextBar('CHRIS/CME_CL1'))
    print(test.getLatestBar('CHRIS/CME_GC1'))
    print(test.peekNextBar('CHRIS/CME_GC1'))
    print("Update all bars: "+str(test.dataStatus))
    test.updateAllBars()

