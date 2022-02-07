import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QStackedWidget


class WindowResponsiblePeople(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_people3.ui', self)
        self.setWindowTitle('Лица, ответственные за экологию в России')
        self.show_image()
        self.stackedWidget_people.setCurrentWidget(self.main_page_all_people)
        self.buttonGroup_all_people.buttonClicked.connect(self.change_page)
        self.show_page()

    def show_image(self):
        self.label_cozlov_image.setPixmap(QPixmap('министр.jpg'))
        self.label_photo_cozlov_own.setPixmap(QPixmap('alexander-kozlov.jpg'))
        self.label_photo_anoprienko.setPixmap(QPixmap('Аноприенко3.jpg'))
        self.label_photo_radchenko.setPixmap(QPixmap('Радченко2.jpg'))
        self.label_photo_yastrebov.setPixmap(QPixmap('Ястребов.jpg'))
        self.label_photo_tsiganov.setPixmap(QPixmap('Цыганов.jpg'))
        self.label_photo_tetenkin.setPixmap(QPixmap('Тетенькин 2.jpg'))
        self.label_photo_kerimov.setPixmap(QPixmap('Керимов.jpg'))

    def change_page(self, btn_clicked):
        name = btn_clicked.text()
        if "Козлов" in name:
            self.stackedWidget_people.setCurrentIndex(1)
        elif "Аноприенко" in name:
            self.stackedWidget_people.setCurrentIndex(2)
        elif "Радченко" in name:
            self.stackedWidget_people.setCurrentIndex(3)
        elif "Ястребов" in name:
            self.stackedWidget_people.setCurrentIndex(4)
        elif "Цыганов" in name:
            self.stackedWidget_people.setCurrentIndex(5)
        elif "Тетенькин" in name:
            self.stackedWidget_people.setCurrentIndex(6)
        else:
            self.stackedWidget_people.setCurrentIndex(7)

    def show_page(self):
        self.buttonGroup_back_all_people.buttonClicked.connect(
                                                self.return_main_page)
        self.buttonGroup_cozlov.buttonClicked.connect(self.show_page_cozlov)
        self.buttonGroup_anoprienko.buttonClicked.connect(
                                                self.show_page_anoprienko)
        self.buttonGroup_radchenko.buttonClicked.connect(
                                                self.show_page_radchenko)
        self.buttonGroup_yastrebov.buttonClicked.connect(
                                                self.show_page_yastrebov)
        self.buttonGroup_tsiganov.buttonClicked.connect(
                                                self.show_page_tsiganov)
        self.buttonGroup_tetenkin.buttonClicked.connect(
                                                self.show_page_tetenkin)
        self.buttonGroup_kerimov.buttonClicked.connect(self.show_page_kerimov)

    def return_main_page(self):
        self.stackedWidget_people.setCurrentWidget(self.main_page_all_people)

    def show_page_cozlov(self):
        self.stackedWidget_people.setCurrentWidget(self.page_minister_cozlov)

    def show_page_anoprienko(self):
        self.stackedWidget_people.setCurrentWidget(self.page_anoprienko)

    def show_page_radchenko(self):
        self.stackedWidget_people.setCurrentWidget(self.page_radchenko)

    def show_page_yastrebov(self):
        self.stackedWidget_people.setCurrentWidget(self.page_yastrebov)

    def show_page_tsiganov(self):
        self.stackedWidget_people.setCurrentWidget(self.page_tsiganov)

    def show_page_tetenkin(self):
        self.stackedWidget_people.setCurrentWidget(self.page_tetenkin)

    def show_page_kerimov(self):
        self.stackedWidget_people.setCurrentWidget(self.page_kerimov)
