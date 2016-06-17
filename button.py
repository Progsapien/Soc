from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal


class Button(QLabel):
    clicked = pyqtSignal(str)

    def __init__(self, text, isRed = 0):
        super(Button, self).__init__()
        self.__text = text
        
        # config.
        if(isRed):
            self.__red = 255
            self.__green = 22
            self.__blue = 22
        else:
            self.__red = 23
            self.__green = 136
            self.__blue = 173

        self.setStyleSheet("background-color: rgb("+str(self.__red)+","+str(self.__green)+","+str(self.__blue)+"); color: white;")
        self.setText("<p align='center'>" + text)

    def setCurrentText(self, text):
        if (type(text) == str):
            self.setText("<p align='center'>" + text)

    def enterEvent(self, e):
        self.__green -= 20
        self.setStyleSheet("background-color: rgb("+str(self.__red)+","+str(self.__green)+","+str(self.__blue)+"); color: white;")

    def mousePressEvent(self, e):
        self.__blue -= 20
        self.setStyleSheet("background-color: rgb("+str(self.__red)+","+str(self.__green)+","+str(self.__blue)+"); color: white;")

    def mouseReleaseEvent(self, e):
        self.__blue += 20
        self.setStyleSheet("background-color: rgb("+str(self.__red)+","+str(self.__green)+","+str(self.__blue)+"); color: white;")
        self.clicked.emit(self.__text)

    def leaveEvent(self, e):
        self.__green += 20
        self.setStyleSheet("background-color: rgb("+str(self.__red)+","+str(self.__green)+","+str(self.__blue)+"); color: white;")
