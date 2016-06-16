from PyQt5.QtWidgets import QWidget, QLabel, QListWidget, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap, QFont
from button import Button

class MenuUI(QWidget):
	def __init__(self):
		super(MenuUI, self).__init__()
		
		self.__ob_list_main = QListWidget()

		self.__ob_label_main = QLabel("Социология: Основные понятия и др.")

		self.__ob_button_add = Button("Добавить")
		self.__ob_button_list = Button("Список")

		self.__ob_vlay_main = QVBoxLayout()
		self.__ob_hlay_main = QHBoxLayout()

		self.buttonClicked = 0

		# config;

		self.setLayout(self.__ob_vlay_main)
		self.setFixedSize(800,600)

		self.__ob_vlay_main.addWidget(self.__ob_label_main, 12)
		self.__ob_vlay_main.addLayout(self.__ob_hlay_main, 1)
		self.__ob_hlay_main.addWidget(self.__ob_button_add)
		self.__ob_hlay_main.addWidget(self.__ob_button_list)

		self.__ob_hlay_main.setContentsMargins(0, 0, 0, 0)
		self.__ob_vlay_main.setContentsMargins(0, 0, 0, 0)
		self.__ob_hlay_main.setSpacing(0)

		self.__ob_label_main.setAlignment(Qt.AlignCenter)
		self.__ob_label_main.setMinimumSize(500,300)
		self.__ob_label_main.setStyleSheet("background: rgb(0,0,0,180); color: white;")
		self.__ob_label_main.setFont(QFont("Arial", 21))

		self.__ob_button_list.clicked.connect(self.__onButtonClick)
		self.__ob_button_add.clicked.connect(self.__onButtonClick)

	def __onButtonClick(self):
		if(self.buttonClicked):
			self.buttonClicked(self.sender().text())

	def paintEvent(self, e):
		p = QPainter(self)
		p.drawPixmap(0, 0, self.width(), self.height(), QPixmap("res/backgr.jpg"))
		p.end()