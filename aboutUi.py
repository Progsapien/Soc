from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtCore import Qt
from button import Button

class AboutUI(QWidget):
	def __init__(self):
		super(AboutUI, self).__init__()

		# create objects;

		self.__ob_vlay_main = QVBoxLayout()

		self.__ob_label_title = QLabel()

		self.__ob_text_text = QTextEdit()

		self.__ob_button_back = Button("Назад")

		self.buttonClicked = 0

		# config;

		self.setLayout(self.__ob_vlay_main)
		self.setFixedSize(600,500)

		self.__ob_vlay_main.setSpacing(0)
		self.__ob_vlay_main.addWidget(self.__ob_label_title)
		self.__ob_vlay_main.addWidget(self.__ob_text_text)
		self.__ob_vlay_main.addWidget(self.__ob_button_back)

		self.__ob_button_back.clicked.connect(self.__onButtonClick)
		self.__ob_button_back.setFixedHeight(50)

		self.__ob_label_title.setStyleSheet("background: rgb(74, 176, 74);")
		self.__ob_label_title.setAlignment(Qt.AlignCenter)
		self.__ob_label_title.setFixedHeight(50)

		self.__ob_text_text.setStyleSheet("background: rgb(200, 200, 200); border: none;")
		self.__ob_text_text.setReadOnly(True)


	def __onButtonClick(self):
		self.buttonClicked()

	def showData(self, item):
		self.__ob_label_title.setText(item.getTitle())
		self.__ob_text_text.setText(item.getText())
		self.show()