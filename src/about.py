from Ui_about import Ui_MainWindow
from PyQt6.QtWidgets import QWidget, QMainWindow

class AboutWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

