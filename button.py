from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class Button(QLabel):
    clicked = pyqtSignal(str)

    def __init__(self, text, icon = 0):
        super(Button, self).__init__()
        self.__text = text
        
        # config.

        self.setStyleSheet("background-color: rgb(23,136,173); color: white;")
        self.__data = 0

        if(not icon):
            self.__data = "<p align='center'>" + text
        else:
            self.__data = "<p align='center'><img src='" + icon + "'><br>" + text + "</p>"

        self.setText(self.__data)

    def setCurrentText(self, text):
        if (type(text) == str):
            self.setText("<p align='center'>" + text)

    def enterEvent(self, e):
        self.setStyleSheet("background-color: rgb(23,116,173); color: white;")

    def mousePressEvent(self, e):
        self.setStyleSheet("background-color: rgb(23,116,153); color: white;")

    def mouseReleaseEvent(self, e):
        self.setStyleSheet("background-color: rgb(23,116,173); color: white;")
        self.clicked.emit(self.__text)

    def leaveEvent(self, e):
        self.setStyleSheet("background-color: rgb(23,136,173); color: white;")
