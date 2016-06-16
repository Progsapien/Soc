from PyQt5.QtWidgets import QWidget, QListWidget, QLineEdit, QVBoxLayout
from PyQt5.QtGui import *
from button import Button

class ListUI(QWidget):
	def __init__(self, socman):
		super(ListUI, self).__init__()

		# create objects;

		self.__socman = socman

		self.__ob_list_main = QListWidget()

		self.__ob_line_search = QLineEdit()

		self.__ob_vlay_main = QVBoxLayout()

		self.__ob_button_main = Button("Назад")

		self.buttonClicked = 0
		self.doubleClicked = 0

		#config;

		self.setLayout(self.__ob_vlay_main)
		self.setFixedSize(700, 500)

		self.__ob_vlay_main.setSpacing(0)
		self.__ob_vlay_main.addWidget(self.__ob_line_search)
		self.__ob_vlay_main.addWidget(self.__ob_list_main)
		self.__ob_vlay_main.addWidget(self.__ob_button_main)

		self.__ob_line_search.setStyleSheet("background: rgb(170, 170, 170); border: none;")
		self.__ob_line_search.setFixedHeight(50)
		self.__ob_line_search.textChanged.connect(self.__onLineEdit)

		self.__ob_list_main.setStyleSheet("background: rgb(200, 200, 200); border: none;")
		self.__ob_list_main.setMinimumWidth(self.__ob_list_main.sizeHintForColumn(0))
		self.__ob_list_main.itemDoubleClicked.connect(self.__onDoubleClicked)

		self.__ob_button_main.clicked.connect(self.__onButtonClicked)
		self.__ob_button_main.setFixedHeight(50)

	def showData(self):
		self.__ob_list_main.clear()
		self.__ob_line_search.clear()
		for i in self.__socman.getDump():
			self.__ob_list_main.addItem(i.getTitle())
		self.show()

	def __onButtonClicked(self):
		self.buttonClicked()

	def __onLineEdit(self):
		if(len(self.__ob_line_search.text())):
			self.__ob_list_main.clear()
			for i in self.__socman.getDump():
				if(self.__ob_line_search.text() in i.getTitle()):
					self.__ob_list_main.addItem(i.getTitle())
		else:
			self.__ob_list_main.clear()
			for i in self.__socman.getDump():
				self.__ob_list_main.addItem(i.getTitle())

	def __onDoubleClicked(self, item):
		for i in self.__socman.getDump():
			if(item.text() == i.getTitle()):
				self.doubleClicked(i)
				break
