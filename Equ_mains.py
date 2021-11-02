import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from ui import menu_ui as menu
from conf.pH1_conf import *

class MainWindow(QMainWindow):
    def __init__(self):
            super().__init__()
            self.ui = menu.Ui_Equitmen()
            self.ui.setupUi(self)
            self.ui.pH_1.clicked.connect(self.ph_1)

    def ph_1(self):
        self.childwindow = ph_1()
        self.childwindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindos=MainWindow()
    mainWindos.show()
    app.exec()
