from PyQt6 import QtWidgets as QtW
from src.gui.main_window import MainWindow

class App(QtW.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MainWindow()
        self.window.show()

