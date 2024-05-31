from dataHandler.downloader import DataDownloader
from dataHandler.preprocessor import Preprocessor

import pandas as pd
from sklearn import model_selection

class Dataset:
    def __init__(self) -> None:
        self.downloader = DataDownloader()
        self.preprocessor = Preprocessor()

    def getWorldIndexes(self):
        df = self.downloader.htmlData(url = self.downloader.worldIndexes, columns = self.downloader.worldIndexesColumns)
        return df

    def getMarketCompounds(self, marketTicker):
        url = "http://uk.finance.yahoo.com/quote/" + marketTicker + "/components"
        df = self.downloader.htmlData(url = url, columns = slice(None))
        return df
    
    def getStockData(self, stock, pathToSave = ""):
        url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock + "?period1=583718400&period2=1716768000&interval=1d&events=history&includeAdjustedClose=true"
        df = self.downloader.downloadCSV(url = url)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index("Date", inplace = True)
        print(df)
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
        columns = df.columns
        df = self.preprocessor.dropUnnamedColumn(df)
        df = self.preprocessor.dropDuplicates(df)
        df[columns[1:]] = self.preprocessor.fillMissingData(df[columns[1:]])
        df[columns[1:]] = self.preprocessor.scaleData(df[columns[1:]])
        df = self.preprocessor.sortValuesByDate(df)
        df.set_index("Date", inplace = True)
        self._splitDataset(df, splitFactor, path, stock)

if __name__=="__main__":
    data = Dataset()
    print(data.getWorldIndexes())