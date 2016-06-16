from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, QLineEdit
from button import Button

class SearchUI(QWidget):
	def __init__(self, searchFunction):
		super(SearchUI, self).__init__()

		# create objects;

		self.__ob_vlay_main = QVBoxLayout()
		self.__ob_line_main = QLineEdit()
		self.__ob_list_main = QListWidget()

		# config;

		self.setLayout(self.__ob_vlay_main)
		self.setStyleSheet("background: rgb(255, 255, 255);")

		self.__ob_line_main.setStyleSheet("border: none; background: rgb(97, 39, 171);")


	def __onLineEdit(self):
		print(self.__search(self.__ob_line_main.text()))