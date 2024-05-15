from gui.window import MainWindow
import multiprocessing

if __name__=="__main__":
   
   p = multiprocessing.Process(MainWindow.run())
   p.start()
   p.join()