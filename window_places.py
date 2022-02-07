import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class WindowPlaces(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_places.ui', self)
        self.setWindowTitle('Места с серьёзно пострадавшей экологией')
        self.initUI()

    def initUI(self):
        self.buttonGroup_cities.buttonClicked.connect(self.change_page)
        self.stackedWidget.setCurrentWidget(self.main_page)
        self.label_photo()

    def label_photo(self):
        self.label_image_city_all.setPixmap(QPixmap('город_обложка.jpg'))
        self.label_photo_krasnoyarsk.setPixmap(QPixmap('Красноярск.jpg'))
        self.label_photo_magnitogorsk.setPixmap(QPixmap('магнитогорск.jpg'))
        self.label_photo_norilsk.setPixmap(QPixmap('Норильск.jpg'))
        self.label_photo_lipetsk.setPixmap(QPixmap('Липецк.jpg'))
        self.label_photo_cherepovets.setPixmap(QPixmap('Череповец.jpg'))
        self.label_photo_novokuznetsk.setPixmap(QPixmap('Новокузнецк.jpg'))
        self.label_photo_nizhniy_tagil.setPixmap(QPixmap('Нижний Тагил.jpg'))
        self.label_photo_omsk.setPixmap(QPixmap('Омск.jpg'))
        self.label_photo_chelyabinsk.setPixmap(QPixmap('Челябинск.jpg'))
        self.label_photo_dzerzhinsk.setPixmap(QPixmap('Дзержинск.jpg'))
        self.label_photo_bratsk.setPixmap(QPixmap('Братск.jpg'))
        self.label_photo_chita.setPixmap(QPixmap('Чита.jpg'))
        self.label_photo_mednogorsk.setPixmap(QPixmap('Медногорск.jpg'))
        self.label_photo_novocherkassk.setPixmap(QPixmap('Новочеркасск.jpg'))
        self.label_photo_asbest.setPixmap(QPixmap('Асбест.jpg'))

    def change_page(self, btn_clicked):
        city = btn_clicked.text()
        if 'Красноярск' in city:
            self.stackedWidget.setCurrentWidget(self.page_krasnoyarsk)
        elif 'Магнитогорск' in city:
            self.stackedWidget.setCurrentWidget(self.page_magnitogorsk)
        elif 'Норильск' in city:
            self.stackedWidget.setCurrentWidget(self.page_norilsk)
        elif 'Липецк' in city:
            self.stackedWidget.setCurrentWidget(self.page_lipetsk)
        elif 'Череповец' in city:
            self.stackedWidget.setCurrentWidget(self.page_cherepovets)
        elif 'Новокузнецк' in city:
            self.stackedWidget.setCurrentWidget(self.page_novokuznetsk)
        elif 'Нижний Тагил' in city:
            self.stackedWidget.setCurrentWidget(self.page_nizhniy_tagil)
        elif 'Омск' in city:
            self.stackedWidget.setCurrentWidget(self.page_omsk)
        elif 'Челябинск' in city:
            self.stackedWidget.setCurrentWidget(self.page_chelyabinsk)
        elif 'Дзержинск' in city:
            self.stackedWidget.setCurrentWidget(self.page_dzerzhinsk)
        elif 'Братск' in city:
            self.stackedWidget.setCurrentWidget(self.page_bratsk)
        elif 'Чита' in city:
            self.stackedWidget.setCurrentWidget(self.page_chita)
        elif 'Медногорск' in city:
            self.stackedWidget.setCurrentWidget(self.page_mednogorsk)
        elif 'Новочеркасск' in city:
            self.stackedWidget.setCurrentWidget(self.page_novocherkassk)
        else:
            self.stackedWidget.setCurrentWidget(self.page_asbest)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            n = self.stackedWidget.currentIndex()
            self.stackedWidget.setCurrentIndex(n - 1)
        if event.key() == Qt.Key_Right:
            n = self.stackedWidget.currentIndex()
            self.stackedWidget.setCurrentIndex(n + 1)

    def keyPressEvent(self, event):
        n = self.stackedWidget.currentIndex()
        if event.key() == Qt.Key_Left:
            if n == 0:
                self.stackedWidget.setCurrentIndex(15)
            else:
                self.stackedWidget.setCurrentIndex(n - 1)
        if event.key() == Qt.Key_Right:
            if n == 15:
                self.stackedWidget.setCurrentIndex(0)
            else:
                self.stackedWidget.setCurrentIndex(n + 1)
