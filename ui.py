from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QListWidget, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class Ui(QWidget):
	def __init__(self):
		super(Ui, self).__init__()

		# create objects;

		self.__ob_list_main = QListWidget()

		self.__ob_label_main = QLabel("Soc")

		self.__ob_button_add = QPushButton("Добавить")
		self.__ob_button_list = QPushButton("Список")

		self.__ob_vlay_main = QVBoxLayout()
		self.__ob_hlay_main = QHBoxLayout()

		self.__ob_line_main = QLineEdit()

		# config;

		self.setLayout(self.__ob_vlay_main)

		self.__ob_vlay_main.addWidget(self.__ob_label_main)
		self.__ob_vlay_main.addLayout(self.__ob_hlay_main)
		self.__ob_hlay_main.addWidget(self.__ob_line_main, 3)
		self.__ob_hlay_main.addWidget(self.__ob_button_add,1)
		self.__ob_hlay_main.addWidget(self.__ob_button_list,1)

		self.__ob_label_main.setAlignment(Qt.AlignCenter)
		self.__ob_label_main.setMinimumSize(500,300)

		self.__ob_line_main.setStyleSheet("background: rgb(200, 200, 200); border: none;")
		self.__ob_line_main.setMinimumHeight(50)
