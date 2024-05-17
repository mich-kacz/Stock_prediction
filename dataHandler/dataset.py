from dataHandler.downloader import DataDownloader

import pandas as pd

class Dataset:
    def __init__(self) -> None:
        self.downloader = DataDownloader()

    def getWorldIndexes(self):
        df = self.downloader.htmlData(columns = self.downloader.worldIndexesColumns)
        return df

if __name__=="__main__":
    data = Dataset()
    print(data.getWorldIndexes())