from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QSize
from button import Button

class ListUI(QWidget):
	def __init__(self, socman):
		super(ListUI, self).__init__()

		# create objects;

		self.__socman = socman

		self.__ob_list_main = QListWidget()

		self.__ob_line_search = QLineEdit()

		self.__ob_vlay_main = QVBoxLayout()
		self.__ob_hlay_main = QHBoxLayout()

		self.__ob_button_back = Button("Назад")
		self.__ob_button_delete = Button("Удалить", 1)

		self.buttonClicked = 0
		self.doubleClicked = 0

		#config;

		self.setLayout(self.__ob_vlay_main)
		self.setFixedSize(700, 500)

		self.__ob_vlay_main.setSpacing(0)
		self.__ob_vlay_main.addWidget(self.__ob_line_search)
		self.__ob_vlay_main.addWidget(self.__ob_list_main)
		self.__ob_vlay_main.addLayout(self.__ob_hlay_main)
		self.__ob_hlay_main.addWidget(self.__ob_button_back, 4)
		self.__ob_hlay_main.addWidget(self.__ob_button_delete, 1)


		self.__ob_line_search.setStyleSheet("background: rgb(170, 170, 170); border: none;")
		self.__ob_line_search.setFixedHeight(50)
		self.__ob_line_search.textChanged.connect(self.__onLineEdit)

		self.__ob_list_main.setStyleSheet("background: rgb(200, 200, 200); border: none;")
		self.__ob_list_main.setMinimumWidth(self.__ob_list_main.sizeHintForColumn(0))
		self.__ob_list_main.itemDoubleClicked.connect(self.__onDoubleClicked)
		self.__ob_list_main.itemClicked.connect(self.__onItemClicked)
		self.__ob_list_main.setSelectionMode(QListWidget.MultiSelection)

		self.__ob_button_back.clicked.connect(self.__onButtonClicked)
		self.__ob_button_back.setFixedHeight(50)
		self.__ob_button_delete.hide()
		self.__ob_button_delete.clicked.connect(self.__onButtonDeleteClicked)

	def showData(self):
		self.loadList()
		self.show()

	def __onButtonClicked(self):
		self.buttonClicked()

	def __onLineEdit(self):
		self.__ob_button_delete.hide()
		if(len(self.__ob_line_search.text())):
			self.__ob_list_main.clear()
			for i in self.__socman.getDump():
				if(self.__ob_line_search.text().upper() in i.getTitle().upper()):
					item = QListWidgetItem()
					item.setText(i.getTitle())
					item.setSizeHint(QSize(10,30))
					self.__ob_list_main.addItem(item)
		else:
			self.loadList()

	def __onDoubleClicked(self, item):
		self.__ob_list_main.clearSelection()
		for i in self.__socman.getDump():
			if(item.text() == i.getTitle()):
				self.doubleClicked(i)
				break

	def __onItemClicked(self):
		if(len(self.__ob_list_main.selectedItems())):
			self.__ob_button_delete.show()
		else:
			self.__ob_button_delete.hide()

	def __onButtonDeleteClicked(self):
		for i in self.__ob_list_main.selectedItems():
			for item in self.__socman.getDump():
				if(i.text() == item.getTitle()):
					self.__socman.delete(item)
					break
		self.__ob_button_delete.hide()
		self.loadList()

	def loadList(self):
		self.__ob_list_main.clear()
		self.__ob_line_search.clear()
		for i in self.__socman.getDump():
			item = QListWidgetItem()
			item.setText(i.getTitle())
			item.setSizeHint(QSize(10,30))
			self.__ob_list_main.addItem(item)
