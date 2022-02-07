import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

from constants import D


class WindowTop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_top.ui', self)
        self.setWindowTitle('Топ стран по экологии')
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect('top_countries.sqlite')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS top_countries
                        (№ INT, Country TEXT,Ind INT, Population INT)''')
        self.table = self.cur.execute("""SELECT *
                            FROM top_countries""").fetchall()
        self.show_table()
        self.btn_find.clicked.connect(self.find_country)

    def show_table(self):
        self.table_top.setColumnCount(3)
        self.table_top.setRowCount(106)
        for i in self.table:
            for j, elem in enumerate(i[1:]):
                self.table_top.setItem(i[0] - 1, j,
                                       QTableWidgetItem(str(elem)))
        self.table_top.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)
        self.con.commit()

    def find_country(self):
        self.country = self.lineEdit_input_country.text().strip()
        self.countries = self.cur.execute("""SELECT Country
                                FROM top_countries""").fetchall()
        self.list_countries = []
        self.check_name()
        if self.country not in self.list_countries:
            self.lineEdit_answer.setText('Простите, но данных по\
                                         этой стране нет.')
        else:
            self.answer = self.cur.execute("""SELECT  *
                                FROM top_countries WHERE Country = ?""",
                                           (self.country,)).fetchone()
            self.s = ''
            for i in self.answer:
                self.s += str(i) + '      '
            self.lineEdit_answer.setText(self.s)

    def check_name(self):
        for i in self.countries:
            for j in i:
                self.list_countries.append(j)
        for i in self.list_countries:
            if i.lower() == self.country.lower():
                self.country = i

        for i in D.keys():
            if self.country.lower() == i:
                self.country = D[i]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.find_country()

    def closeEvent(self, event):
        self.con.close()
