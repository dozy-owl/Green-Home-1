import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

from window_top import *
from window_your_input import *
from window_people import *
from window_places import *

        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Зелёный дом')
        self.pixmap = QPixmap('i.jpg')
        self.image.setPixmap(self.pixmap)
        self.btn_run()

    def btn_run(self):
        self.btn_top.clicked.connect(self.window_top)
        self.btn_your.clicked.connect(self.window_your_input)
        self.btn_places.clicked.connect(self.window_places)
        self.btn_resp_people.clicked.connect(self.window_resp_people)
        self.btn_look_state_of_ecology.clicked.connect(self.look_state_of_ecology)

    def window_top(self):
        self.wind_top = WindowTop()
        self.wind_top.show()

    def window_your_input(self):
        self.wind_your_input = WindowYourInput()
        self.wind_your_input.show()

    def window_places(self):
        self.wind_places = WindowPlaces()
        self.wind_places.show()

    def window_resp_people(self):
        self.wind_resp_people = WindowResponsiblePeople()
        self.wind_resp_people.show()

    def look_state_of_ecology(self):
        title = self.combo_state_of_ecology.currentText()
        if "Основные" in title:
            self.wind_state_of_ecology = WindowMainIndicators()
        elif "Причины" in title:
            self.wind_state_of_ecology = WindowReasons()
        else:
            self.wind_state_of_ecology = WindowWays()
        self.wind_state_of_ecology.show()
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
