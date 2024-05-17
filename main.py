from gui.window import MainWindow
from dataHandler.dataset import Dataset

import multiprocessing

if __name__=="__main__":
   
#   p = multiprocessing.Process(MainWindow.run())
#   p.start()
#   p.join()
   dataset = Dataset()
   MainWindow.run(dataset.getWorldIndexes())