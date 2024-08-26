from gui.window import MainWindow
from dataHandler.dataset import Dataset
from predictor.predictor import Predictor

import threading
import time


class Engine:


    def __init__(self) -> None:
        self.dataset = Dataset()
        self.window = MainWindow(self.dataset.getWorldIndexes(), self.stateMachine)
        self.state = "Idle"#"DataDownloaded" # Change to Idle in final version
        self.periodicFlag = 1
        self.stock = "RR.L" #Change in final version

    def run(self):
        self._t1 = threading.Thread(target=self._periodicStateCheck)
        self._t1.daemon = True  # Daemonize the thread so it exits when the main thread exits
        self._t1.start()
        self.window.run()

    def _periodicStateCheck(self):
        while self.periodicFlag == 1:
            time.sleep(1)
            if self.state == "DataDownloaded":
                self.stateMachine("StartPreprocessing")

    def stateMachine(self, event):

        if event == "MarketClick":
            if self.state == "Idle" or self.state == "ChoosingStock":
                df = self.dataset.getMarketCompounds(self.window.getChoosenMarket())
                self.window.setTickersForMarket(df)
                self.state = "ChoosingStock"
        elif event == "StockChoosen":
            if self.state == "ChoosingStock":
                self.stock = self.window.getChoosenStock()
                df = self.dataset.getStockData(self.stock, "data/")
                self.state = "DataDownloaded"
        elif event == "StartPreprocessing":
            self.dataset.preprocessHistData("data/", self.stock)
            self.state = "DataReady"
            print("RDY")
        elif event == "PlotPrediction":
            predictor = Predictor(self.window.modelID, self.dataset.preprocessor.scaler)
            predictions, real, dates, datesX = predictor(self.dataset.dataset)
            self.window.plotGraph(dates, datesX, predictions, real)

        elif event == "Closing":
            print("Closing")
            self.periodicFlag = 0
            self._t1.join()
            print("Closed")
        else:
            pass