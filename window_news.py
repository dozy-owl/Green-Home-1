import sys
import requests
from bs4 import BeautifulSoup

from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QTextEdit

from constants import URL, CLASS_TEXT_ALL


class WindowNews(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window_news.ui', self)
        self.setWindowTitle('Главные новости')
        self.initUI()

    def initUI(self):
        self.title = []
        self.text = []
        self.date = []
        self.get_info()
        self.show_news()

    def get_info(self):
        response = requests.get(URL)
        if response.status_code == 200:
            self.title = []
            self.text = []
            self.date = []
            soup = BeautifulSoup(response.content, "html.parser")
            text_all = soup.find_all("div", class_=CLASS_TEXT_ALL)
            for i in text_all:
                if "search-item__text" in str(i):
                    i = str(i).split()
                    date = i[i.index('class="search-item__category">') + 1:
                             i.index('</span>')]
                    date = ' '.join(date)
                    title = i[i.index('class="search-item__link-in">') + 2:
                              i.index('class="search-item__text">') - 1]
                    title[0] = title[0][title[0].find('>') + 1:]
                    title[-1] = title[-1][:title[-1].find('<')]
                    title = ' '.join(title)
                    i = i[i.index('class="search-item__text">') + 1:]
                    text = i[: i.index('</span>')]
                    text = ' '.join(text)
                    self.title.append(title)
                    self.text.append(text)
                    self.date.append(date)

    def show_news(self):
        for i in range(5):
            text_news = QTextEdit(self)
            text_news.resize(832, 130)
            if i == 0:
                text_news.move(10, 71)
            else:
                text_news.move(10, 130 * i + 71)
            text_news.setReadOnly(True)
            text_news.setText(f'<b>{str(self.title[i])}</b>. ' +
                              str(self.text[i]) + '. ' +
                              f'<i>{str(self.date[i])}</i>')
            text_news.setFont(QFont('Times New Roman', 12))

    def closeEvent(self, event):
        self.title = []
        self.date = []
        self.date = []
