import sys
import pandas as pd

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from gui.uiMainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, marketNames : pd.DataFrame):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.setMarketNames(marketNames)
    def run(marketNames : pd.DataFrame):
        app = QApplication(sys.argv)

        window = MainWindow(marketNames)
        window.show()

        sys.exit(app.exec())
    