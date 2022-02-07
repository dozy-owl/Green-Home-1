import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class WindowLandfillSites(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_landfill_sites.ui', self)
        self.setWindowTitle('Отбросы и общество')
        self.label_photo_landfill_main.setPixmap(QPixmap(
                                                'свалки_главная2.jpg'))
        self.buttonGroup_content.buttonClicked.connect(self.show_page)
        self.buttonGroup_big_dumps.buttonClicked.connect(self.show_page_dump)
        self.stackedWidget_waste.setCurrentIndex(0)
        self.buttonGroup_return_dumps.buttonClicked.connect(
                                                self.return_page_wastes)

    def show_page(self, btn_clicked):
        title = btn_clicked.text()
        if 'Немного цифр' == title:
            self.stackedWidget_waste.setCurrentIndex(0)
        elif 'Площадь' in title:
            self.stackedWidget_waste.setCurrentIndex(1)
        elif 'Ситуация' in title:
            self.stackedWidget_waste.setCurrentIndex(2)
        elif 'Сколько мусора' in title:
            self.stackedWidget_waste.setCurrentIndex(3)
        elif 'девается?' in title:
            self.stackedWidget_waste.setCurrentIndex(4)
        elif 'Количество свалок' in title:
            self.stackedWidget_waste.setCurrentIndex(5)
        elif 'Что об этом думают' in title:
            self.stackedWidget_waste.setCurrentIndex(6)
        elif 'Мусор в России' in title:
            self.stackedWidget_waste.setCurrentIndex(7)
        elif 'Переработка' in title:
            self.stackedWidget_waste.setCurrentIndex(9)
        else:
            self.stackedWidget_waste.setCurrentIndex(8)

    def show_page_dump(self, btn):
        dump = btn.text()
        if 'Красный Бор' in dump:
            self.stackedWidget_waste.setCurrentIndex(10)
        elif 'Игумновский' in dump:
            self.stackedWidget_waste.setCurrentIndex(11)
        elif 'Урюпинска' in dump:
            self.stackedWidget_waste.setCurrentIndex(12)
        elif 'Кулаковский' in dump:
            self.stackedWidget_waste.setCurrentIndex(13)
        elif 'Подмосковье' in dump:
            self.stackedWidget_waste.setCurrentIndex(14)
        elif 'Саратовом' in dump:
            self.stackedWidget_waste.setCurrentIndex(15)
        elif 'Свердловской' in dump:
            self.stackedWidget_waste.setCurrentIndex(17)
        elif 'Шушары' in dump:
            self.stackedWidget_waste.setCurrentIndex(18)
        elif 'Широкоречная' in dump:
            self.stackedWidget_waste.setCurrentIndex(19)
        elif 'Новгородской' in dump:
            self.stackedWidget_waste.setCurrentIndex(16)

    def return_page_wastes(self):
        self.stackedWidget_waste.setCurrentIndex(8)
