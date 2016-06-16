from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from menuUi import MenuUI
from addUi import AddUI
from listUi import ListUI
from aboutUi import AboutUI

class Ui(QWidget):
	def __init__(self, socman):
		super(Ui, self).__init__()

		# create objects;

		self.__ob_vlay_main = QVBoxLayout()

		self.__ob_widget_menu = MenuUI()
		self.__ob_widget_add = AddUI(socman)
		self.__ob_widget_list = ListUI(socman)
		self.__ob_widget_about = AboutUI()

		# config;

		self.setLayout(self.__ob_vlay_main)
		self.setFixedSize(800,600)
		self.setWindowTitle("Социлогия: основные понятия и др.")

		self.__ob_widget_menu.buttonClicked = self.__onMenuClicked

		self.__ob_widget_add.buttonClicked = self.__onAddClicked

		self.__ob_widget_list.buttonClicked = self.__onListClicked
		self.__ob_widget_list.doubleClicked = self.__onDoubleClicked

		self.__ob_widget_about.buttonClicked = self.__onAboutClicked

		self.__ob_vlay_main.addWidget(self.__ob_widget_menu)
		self.__ob_vlay_main.setAlignment(Qt.AlignCenter)
		self.__ob_vlay_main.setContentsMargins(0, 0, 0, 0)

	def __onMenuClicked(self, text):
		if(text == "<p align='center'>Добавить"):
			self.__ob_widget_menu.hide()
			self.__ob_vlay_main.removeWidget(self.__ob_widget_menu)
			self.__ob_vlay_main.addWidget(self.__ob_widget_add)
			self.__ob_widget_add.show()
		elif(text == "<p align='center'>Список"):
			self.__ob_widget_menu.hide()
			self.__ob_vlay_main.removeWidget(self.__ob_widget_menu)
			self.__ob_vlay_main.addWidget(self.__ob_widget_list)
			self.__ob_widget_list.showData()

	def __onAddClicked(self):
		self.__ob_widget_add.hide()
		self.__ob_vlay_main.removeWidget(self.__ob_widget_add)
		self.__ob_vlay_main.addWidget(self.__ob_widget_menu)
		self.__ob_widget_menu.show()

	def __onListClicked(self):
		self.__ob_widget_list.hide()
		self.__ob_vlay_main.removeWidget(self.__ob_widget_list)
		self.__ob_vlay_main.addWidget(self.__ob_widget_menu)
		self.__ob_widget_menu.show()

	def __onDoubleClicked(self, item):
		self.__ob_widget_list.hide()
		self.__ob_vlay_main.removeWidget(self.__ob_widget_list)
		self.__ob_vlay_main.addWidget(self.__ob_widget_about)
		self.__ob_widget_about.showData(item)

	def __onAboutClicked(self):
		self.__ob_widget_about.hide()
		self.__ob_vlay_main.removeWidget(self.__ob_widget_about)
		self.__ob_vlay_main.addWidget(self.__ob_widget_list)
		self.__ob_widget_list.showData()