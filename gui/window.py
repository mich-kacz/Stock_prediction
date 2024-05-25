import sys
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

    def run(self):

        #window = MainWindow(marketNames)
        self.show()

        sys.exit(self.app.exec())

    def tableCallback(self, item):
        self.marketName = item
        self.eventCallback("MarketClick")
        self.ui.setCompounds(self.TickersForMarket)

    def buttonCallback(self):
        pass

    def getChoosenMarket(self):
        return self.marketName
    def setTickersForMarket(self, tickers : pd.DataFrame):
        self.TickersForMarket = tickers
    