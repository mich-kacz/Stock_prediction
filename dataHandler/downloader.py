import pandas as pd

import requests
from io import StringIO

class DataDownloader:
    worldIndexes = "https://finance.yahoo.com/world-indices"
    worldIndexesColumns = ["Symbol", "Price", "Change %"]#, "Name"]

    def __init__(self) -> None:
        pass

    def htmlData(self, url, columns) -> pd.DataFrame:
        r = requests.get(url, headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        html = StringIO(r.text)
        df = pd.read_html(html)[0]
        return df[columns]
    
    def downloadCSV(self, url) -> pd.DataFrame:
        df = pd.read_csv(url)
        return df