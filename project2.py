import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

from window_top import *
from window_your_input import *
from window_people import *
from window_places import *
from window_state_of_ecology import *
from window_landfill_sites import *
from window_news import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project2.ui', self)
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
        self.btn_state_of_ecology.clicked.connect(self.window_state_of_ecology)
        self.btn_landfill_sites.clicked.connect(self.window_landfill_sites)
        self.btn_news.clicked.connect(self.window_news)

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

    def window_state_of_ecology(self):
        self.wind_state_of_ecology = WindowStateOfEcology()
        self.wind_state_of_ecology.show()

    def window_landfill_sites(self):
        self.wind_landfill_sites = WindowLandfillSites()
        self.wind_landfill_sites.show()

    def window_news(self):
        self.wind_news = WindowNews()
        self.wind_news.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
