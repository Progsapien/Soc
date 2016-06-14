from PyQt5.QtWidgets import QWidget, QVBoxLayout
from menuUi import MenuUI

class Ui(QWidget):
	def __init__(self):
		super(Ui, self).__init__()

		# create objects;

		self.__ob_vlay_main = QVBoxLayout()
		self.__ob_widget_menu = MenuUI()

		# config;

		self.setLayout(self.__ob_vlay_main)

		self.__ob_widget_menu.buttonClicked = self.__onMenuClicked

		self.__ob_vlay_main.addWidget(self.__ob_widget_menu)
		self.__ob_vlay_main.setContentsMargins(0, 0, 0, 0)

	def __onMenuClicked(self, text):
		if(text == "<p align='center'>Добавить"):
			print("ADD")
		else:
			print("LIST")