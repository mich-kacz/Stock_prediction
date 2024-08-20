import sys
from PySide6.QtGui import QCloseEvent
import pandas as pd
from dataHandler.dataset import Dataset

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from gui.uiMainWindow import Ui_MainWindow

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QMainWindow):
    def __init__(self, marketNames : pd.DataFrame, eventCallback):
        self.app = QApplication(sys.argv)
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.registerCallbacks(self.tableCallback, self.buttonCallback, self.buttonPrediction)
        self.ui.setupUi(self)
        self.ui.setMarketNames(marketNames)
        self.eventCallback = eventCallback
        self.marketName = None
        self.TickersForMarket = None
        self.stockName = None
        self.modelID = None


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
        self.modelID = self.ui.getModelName()
        self.eventCallback("StockChoosen")

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ui.addPlotToWidget(self.canvas)
        self._plotDummyGraph()

    def buttonPrediction(self):
        self.eventCallback("PlotPrediction")

    def getChoosenMarket(self):
        return self.marketName
    def getChoosenStock(self):
        return self.stockName
    def setTickersForMarket(self, tickers : pd.DataFrame):
        self.TickersForMarket = tickers
    

    def _plotDummyGraph(self):
        # Clear the figure
        self.figure.clear()
        # Create an axis
        ax = self.figure.add_subplot(111)
        ax.set_title("Price prediction - " + self.stockName)
        ax.grid()
        # Plot data
        ax.plot([0, 1, 2, 3, 4], [0, 0, 0, 0, 0])
        # Refresh canvas
        self.canvas.draw()

    def plotGraph(self, dates, datesX, predictions, real):
        # Clear the figure
        self.figure.clear()
        # Create an axis
        ax = self.figure.add_subplot(111)
        ax.set_title("Price prediction - " + self.stockName)
        ax.grid()
        # Plot data
        ax.plot(dates, real)
        ax.plot(datesX, predictions)

        
        locator = plt.matplotlib.dates.AutoDateLocator(minticks=5, maxticks=10)
        ax.xaxis.set_major_locator(locator)
        ax.legend(["Real", "Prediction"])
        # Refresh canvas
        self.canvas.draw()