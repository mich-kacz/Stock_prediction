from gui.window import MainWindow
from dataHandler.dataset import Dataset


class Engine:


    def __init__(self) -> None:
        self.dataset = Dataset()
        self.window = MainWindow(self.dataset.getWorldIndexes(), self.stateMachine)
        self.state = "Idle"

    def run(self):
        self.window.run()

    def stateMachine(self, event):
        
        if event == "MarketClick":
            if self.state == "Idle":
                df = self.dataset.getMarketCompounds(self.window.getChoosenMarket())
                self.window.setTickersForMarket(df)