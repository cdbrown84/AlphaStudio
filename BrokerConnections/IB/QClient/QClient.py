from ibapi.client import EClient

class QClient(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)