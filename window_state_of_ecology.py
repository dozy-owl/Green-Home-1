import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QHeaderView
from PyQt5.QtWidgets import QComboBox, QPushButton, QTableWidgetItem
from PyQt5.QtWidgets import QTableView


class WindowStateOfEcology(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('state.ui', self)
        self.initUI()

    def initUI(self):
        self.tabWidget.setTabText(0, 'Основные показатели экологии')
        self.tabWidget.setTabText(1, 'Причины возникновения')
        self.tabWidget.setTabText(2, 'Пути решения экологических проблем')
        self.tabWidget.setCurrentWidget(self.tab_indicators)
        self.btn_look.clicked.connect(self.show_page_indicators)
        self.stackedWidget_indicators.setCurrentWidget(self.page_state_main)
        self.buttonGroup_content_way.buttonClicked.connect(self.show_page_ways)
        self.stackedWidget_ways.setCurrentIndex(0)
        self.stackedWidget_reasons.setCurrentIndex(0)
        self.buttonGroup_ecology_project.buttonClicked.connect(
            self.show_page_project_ecology)
        self.btn_reasons_next.clicked.connect(self.show_page_reasons_next)
        self.btn_reasons_back.clicked.connect(self.show_page_reasons_back)
        self.buttonGroup_back_ecology_project.buttonClicked.connect(
            self.return_back_project_ecology)
        self.connection = sqlite3.connect('air_pollution_level.sqlite')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS air_pollution_level
                        (AQI TEXT, Level TEXT,
                        Degree TEXT,
                        Negative TEXT, Precautions TEXT)''')
        self.table = self.cursor.execute('''SELECT *
                        FROM air_pollution_level''')
        self.show_table()
        self.label_photo_ways_main.setPixmap(QPixmap('пути решения.jpg'))
        self.label_photo_state.setPixmap(QPixmap(
            'состояние экологии России.jpeg'))

    def show_table(self):
        self.table_aqi.setColumnCount(4)
        self.table_aqi.setRowCount(0)
        for i, row in enumerate(self.table):
            self.table_aqi.setRowCount(
                self.table_aqi.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table_aqi.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.table_aqi.horizontalHeader().setSectionResizeMode(
            2, QHeaderView.ResizeToContents)
        self.table_aqi.horizontalHeader().setSectionResizeMode(
            3, QHeaderView.ResizeToContents)
        self.table_aqi.horizontalHeader().setSectionResizeMode(
            4, QHeaderView.ResizeToContents)
        self.connection.commit()

    def show_page_indicators(self):
        water_text = self.combo_water.currentText()
        soil_text = self.combo_soil.currentText()
        rbtn_checked = self.buttonGroup_rbtn_tab_indicators.checkedButton()
        rbtn_checked_text = rbtn_checked.text()
        if 'воздуха' in rbtn_checked_text:
            if 'Индекс' in self.combo_air.currentText():
                self.stackedWidget_indicators.setCurrentIndex(1)
            elif 'Характерные' in self.combo_air.currentText():
                self.stackedWidget_indicators.setCurrentIndex(2)
            else:
                self.stackedWidget_indicators.setCurrentIndex(3)
        elif 'воды' in rbtn_checked_text:
            if 'Росгидрометр' == water_text:
                self.stackedWidget_indicators.setCurrentIndex(4)
            elif 'Миссия' in water_text:
                self.stackedWidget_indicators.setCurrentIndex(5)
            elif 'Первая' in water_text:
                self.stackedWidget_indicators.setCurrentIndex(6)
            elif 'Вторая' in water_text:
                self.stackedWidget_indicators.setCurrentIndex(7)
            elif 'Третья' in water_text:
                self.stackedWidget_indicators.setCurrentIndex(8)
            elif 'Реализация' in water_text:
                self.stackedWidget_indicators.setCurrentIndex(9)
            else:
                self.stackedWidget_indicators.setCurrentIndex(10)
        elif 'почвы' in rbtn_checked_text:
            if 'Заявление' in soil_text:
                self.stackedWidget_indicators.setCurrentIndex(11)
            elif 'Информация' in soil_text:
                self.stackedWidget_indicators.setCurrentIndex(12)
            elif 'металлами' in soil_text:
                self.stackedWidget_indicators.setCurrentIndex(13)
            elif 'фтора' in soil_text:
                self.stackedWidget_indicators.setCurrentIndex(14)
            elif 'нефтепродуктами' in soil_text:
                self.stackedWidget_indicators.setCurrentIndex(15)
            elif 'нитратами' in soil_text:
                self.stackedWidget_indicators.setCurrentIndex(16)
            else:
                self.stackedWidget_indicators.setCurrentIndex(17)

    def show_page_ways(self, btn_clicked):
        name = btn_clicked.text()
        if 'Национальный' in name:
            self.stackedWidget_ways.setCurrentIndex(1)
        elif 'мониторинг' in name:
            self.stackedWidget_ways.setCurrentIndex(2)
        elif 'стандарты' in name:
            self.stackedWidget_ways.setCurrentIndex(3)
        elif 'Ликвидация' in name:
            self.stackedWidget_ways.setCurrentIndex(4)
        elif 'губернаторов' in name:
            self.stackedWidget_ways.setCurrentIndex(5)
        elif 'Реформа' in name:
            self.stackedWidget_ways.setCurrentIndex(6)
        elif 'Плата' in name:
            self.stackedWidget_ways.setCurrentIndex(7)
        else:
            self.stackedWidget_ways.setCurrentIndex(8)

    def show_page_reasons_next(self):
        self.stackedWidget_reasons.setCurrentIndex(1)

    def show_page_reasons_back(self):
        self.stackedWidget_reasons.setCurrentIndex(0)

    def show_page_project_ecology(self, btn_clicked):
        title = btn_clicked.text()
        if 'I и II' in title:
            self.stackedWidget_ways.setCurrentIndex(9)
        elif 'туризма' in title:
            self.stackedWidget_ways.setCurrentIndex(10)
        elif 'Чистая страна' == title:
            self.stackedWidget_ways.setCurrentIndex(11)
        elif 'уникальных водных' in title:
            self.stackedWidget_ways.setCurrentIndex(12)
        elif 'Байкал' in title:
            self.stackedWidget_ways.setCurrentIndex(13)
        elif 'Волги' in title:
            self.stackedWidget_ways.setCurrentIndex(14)
        elif 'коммунальными' in title:
            self.stackedWidget_ways.setCurrentIndex(16)
        elif 'Сохранение лесов' in title:
            self.stackedWidget_ways.setCurrentIndex(15)
        else:
            self.stackedWidget_ways.setCurrentIndex(17)

    def return_back_project_ecology(self):
        self.stackedWidget_ways.setCurrentIndex(1)

    def closeEvent(self, event):
        self.connection.close()
