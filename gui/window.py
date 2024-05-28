import sys
from PySide6.QtGui import QCloseEvent
import pandas as pd
from dataHandler.dataset import Dataset

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from gui.uiMainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, marketNames : pd.DataFrame, eventCallback):
        self.app = QApplication(sys.argv)
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.registerCallbacks(self.tableCallback, self.buttonCallback)
        self.ui.setupUi(self)
        self.ui.setMarketNames(marketNames)
        self.eventCallback = eventCallback
        self.marketName = None
        self.TickersForMarket = None
        self.stockName = None

    def run(self):
        #window = MainWindow(marketNames)
        self.show()
        sys.exit(self.app.exec())

    #@override
    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.eventCallback("Closing")
        

    def tableCallback(self, item):
        self.marketName = item
        self.eventCallback("MarketClick")
        self.ui.setCompounds(self.TickersForMarket)

    def buttonCallback(self, item):
        self.stockName = item
        self.eventCallback("StockChoosen")

    def getChoosenMarket(self):
        return self.marketName
    def getChoosenStock(self):
        return self.stockName
    def setTickersForMarket(self, tickers : pd.DataFrame):
        self.TickersForMarket = tickers
    