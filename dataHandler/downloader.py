import pandas as pd

class DataDownloader:
    worldIndexes = "https://finance.yahoo.com/world-indices"
    worldIndexesColumns = ["Symbol", "Name"]
    def __init__(self) -> None:
        pass

    def htmlData(self, url = worldIndexes, columns=["Symbol"]) -> pd.DataFrame:
        df = pd.read_html(url)[0]
        return df[columns]