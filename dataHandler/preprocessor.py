from sklearn import preprocessing
import pandas as pd
import numpy as np
import pickle

class Preprocessor:
    def __init__(self) -> None:
        pass

    def dropUnnamedColumn(self, df):
        if "Unnamed: 0" in df.columns:
            df = df.drop(columns="Unnamed: 0")
        if "Unnamed" in df.columns:
            df = df.drop(columns="Unnamed: 0")
        if "" in df.columns:
            df = df.drop(columns="Unnamed: 0")
        return df
    
    def fillMissingData(self, df):
        df = df.interpolate(method='linear',axis=1, inplace=False)
        return df

    def scaleData(self, df):
        self.scaler = preprocessing.MinMaxScaler()
        df = self.scaler.fit_transform(df)
        pickle.dump(self.scaler, open("dataHandler/scalers/scaler.pickle", "wb"))
        return df
    
    def dropDuplicates(self, df):
        df = df.drop_duplicates(subset="Date", keep='last', inplace=False, ignore_index=True)
        return df
    
    def sortValuesByDate(self, df):
        df = df.sort_values(by = "Date")
        return df
    
    def addChangeFeature(self, df):
        prices = df["Close"]
        change = np.zeros([len(df), 1])
        for i in range(len(df)-1):
            increase = prices[i+1] - prices[i]
            change[i+1] = (increase/prices[i])*100
        df["Change[%]"] = change
        return df
    
    def leaveDataSinceDate(self, df, date = '2017-01-01'):
        return df.loc[(df['Date'] >= date)]