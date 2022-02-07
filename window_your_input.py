import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class WindowYourInput(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_your_input.ui', self)
        self.setWindowTitle('Что Вы можете сделать для \
                            улучшения экологии России')
        self.initUI()

    def initUI(self):
        self.buttonGroup_content.buttonClicked.connect(self.change_page)
        self.stackedWidget_input.setCurrentIndex(0)
        self.show_image()

    def show_image(self):
        self.label_photo_main_page.setPixmap(QPixmap(
                                'дерево_главное_окно.jpg'))
        self.label_introduction.setPixmap(QPixmap('вклад.jpg'))
        self.label_world_day.setPixmap(QPixmap('Всемирный день.jpg'))
        self.label_wwf.setPixmap(QPixmap('wwf.jpg'))
        self.label_greenpeace.setPixmap(QPixmap('greenpeace.jpg'))
        self.label_unep.setPixmap(QPixmap('юнеп.jpg'))
        self.label_world_society_animals.setPixmap(QPixmap(
                                'защита животных.jpg'))

    def change_page(self, btn_clicked):
        page_title = btn_clicked.text()
        if 'Вступление' in page_title:
            self.stackedWidget_input.setCurrentWidget(
                                self.page_introduction)
        elif 'Всемирный день' in page_title:
            self.stackedWidget_input.setCurrentWidget(self.page_world_day)
        elif 'Цели' in page_title:
            self.stackedWidget_input.setCurrentWidget(self.page_goals)
        elif 'WWF' in page_title:
            self.stackedWidget_input.setCurrentWidget(self.page_wwf)
        elif 'Green' in page_title:
            self.stackedWidget_input.setCurrentWidget(self.page_greenpeace)
        elif 'ЮНЕП' in page_title:
            self.stackedWidget_input.setCurrentWidget(self.page_unep)
        elif 'Всемирное общество' in page_title:
            self.stackedWidget_input.setCurrentWidget(
                                self.page_world_society_animals)
        elif 'Пищевые' in page_title:
            self.stackedWidget_input.setCurrentWidget(self.page_food)
        elif 'Водные' in page_title:
            self.stackedWidget_input.setCurrentWidget(self.page_water)
        else:
            self.stackedWidget_input.setCurrentWidget(
                                self.page_not_food_wastes)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            n = self.stackedWidget_input.currentIndex()
            if n == 0:
                self.stackedWidget_input.setCurrentIndex(10)
            else:
                self.stackedWidget_input.setCurrentIndex(n - 1)
        if event.key() == Qt.Key_Right:
            n = self.stackedWidget_input.currentIndex()
            if n == 10:
                self.stackedWidget_input.setCurrentIndex(0)
            else:
                self.stackedWidget_input.setCurrentIndex(n + 1)
