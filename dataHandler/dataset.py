from dataHandler.downloader import DataDownloader

import pandas as pd

class Dataset:
    def __init__(self) -> None:
        self.downloader = DataDownloader()

    def getWorldIndexes(self):
        df = self.downloader.htmlData(url = self.downloader.worldIndexes, columns = self.downloader.worldIndexesColumns)
        return df

    def getMarketCompounds(self, marketTicker):
        url = "http://uk.finance.yahoo.com/quote/" + marketTicker + "/components"
        df = self.downloader.htmlData(url = url, columns = slice(None))
        return df

if __name__=="__main__":
    data = Dataset()
    print(data.getWorldIndexes())