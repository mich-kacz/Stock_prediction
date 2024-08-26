from dataHandler.downloader import DataDownloader
from dataHandler.preprocessor import Preprocessor

import pandas as pd
from sklearn import model_selection

class Dataset:
    def __init__(self) -> None:
        self.downloader = DataDownloader()
        self.preprocessor = Preprocessor()
        self.dataset = 0

    def getWorldIndexes(self):
        df = self.downloader.htmlData(url = self.downloader.worldIndexes, columns = self.downloader.worldIndexesColumns)
        return df

    def getMarketCompounds(self, marketTicker):
        marketTicker = marketTicker.split()[0]
        url = "http://uk.finance.yahoo.com/quote/" + marketTicker + "/components"
        df = self.downloader.htmlData(url = url, columns = slice(None))
        return df
    
    def getStockData(self, stock, pathToSave = ""):
        url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock + "?period1=583718400&period2=1716768000&interval=1d&events=history&includeAdjustedClose=true"
        df = self.downloader.downloadCSV(url = url)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index("Date", inplace = True)
        bl = pd.read_csv("data/Bloomberg/" + stock + ".csv").set_index("Date")
        bl.index = pd.to_datetime(bl.index)
        bl = bl["PE"]
        bl = bl.resample('D')
        bl = bl.ffill()
        bl = bl.bfill()
        df = df.join(bl, how="inner")
        if pathToSave != "":
            df.to_csv(pathToSave + "data/" + stock + ".csv")
        return df
    
    def _splitDataset(self, df, factor, pathToSave = "", stock = ""):
        train, validation = model_selection.train_test_split(df, test_size=factor, shuffle=False)
        validation, test = model_selection.train_test_split(validation, test_size=factor, shuffle=False)
        if pathToSave != "":
            train.to_csv(pathToSave + "train/" + stock + ".csv")
            validation.to_csv(pathToSave + "validation/" + stock + ".csv")
            test.to_csv(pathToSave + "test/" + stock + ".csv")
        return train, validation, test
    
    def preprocessHistData(self, path, stock, splitFactor = 0.2):
        df = pd.read_csv(path + "data/" + stock + ".csv")
        df = self.preprocessor.dropUnnamedColumn(df)
        df = self.preprocessor.leaveDataSinceDate(df, date='2024-01-01')
        df = self.preprocessor.dropDuplicates(df)
        df = self.preprocessor.addChangeFeature(df)
        columns = df.columns
        df[columns[1:]] = self.preprocessor.fillMissingData(df[columns[1:]])
        df[columns[1:]] = self.preprocessor.scaleData(df[columns[1:]])
        df = self.preprocessor.sortValuesByDate(df)
        df.set_index("Date", inplace = True)
        self.dataset = df
        #self._splitDataset(df, splitFactor, path, stock) no need for spliting

if __name__=="__main__":
    data = Dataset()
    print(data.getWorldIndexes())