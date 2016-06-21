from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QTextEdit
from button import Button

class AddUI(QWidget):
	def __init__(self, socman):
		super(AddUI, self).__init__()

		# create objects;

		self.__ob_label_title = QLabel("Заголовок, название:")
		self.__ob_label_text = QLabel("Текст, описание:")

		self.__ob_vlay_main = QVBoxLayout()

		self.__ob_line_title = QLineEdit()
		self.__ob_line_text = QTextEdit()

		self.__ob_button_add = Button("Назад")

		self.__socman = socman

		self.buttonClicked = 0

		# config;

		self.setLayout(self.__ob_vlay_main)
		self.setFixedSize(400,250)

		self.__ob_vlay_main.addWidget(self.__ob_label_title)
		self.__ob_vlay_main.addWidget(self.__ob_line_title)
		self.__ob_vlay_main.addWidget(self.__ob_label_text)
		self.__ob_vlay_main.addWidget(self.__ob_line_text)
		self.__ob_vlay_main.addWidget(self.__ob_button_add)
		self.__ob_vlay_main.setContentsMargins(0, 0, 0, 0)

		self.__ob_button_add.setFixedHeight(50)
		self.__ob_button_add.clicked.connect(self.__onButtonClicked)

		self.__ob_line_text.setStyleSheet("background: rgb(200, 200, 200); border: none;")
		self.__ob_line_title.setStyleSheet("background: rgb(200, 200, 200); border: none;")
		self.__ob_line_title.setFixedHeight(30)
		self.__ob_line_title.textChanged.connect(self.__onLinesEdit)
		self.__ob_line_text.textChanged.connect(self.__onLinesEdit)

	def __onButtonClicked(self):
		if(self.__ob_button_add.text() == "<p align='center'>Назад"):
			self.buttonClicked()
		elif(self.__ob_button_add.text() == "<p align='center'>Добавить"):
			if(self.__socman.add(self.__ob_line_title.text(), self.__ob_line_text.toPlainText())):
				self.__ob_button_add.setCurrentText("Не добавлено!")
			else:
				self.__ob_line_text.clear()
				self.__ob_line_title.clear()
				self.buttonClicked()

	def __onLinesEdit(self):
		if(len(self.__ob_line_title.text())):
			count = 0
			for i in self.__socman.getDump():
				if(self.__ob_line_title.text().upper() != i.getTitle().upper()):
					count += 1
				if(count == len(self.__socman.getDump())):
					if(len(self.__ob_line_text.toPlainText())):
						self.__ob_button_add.setCurrentText("Добавить")
					else:
						self.__ob_button_add.setCurrentText("Назад")
				else:
					self.__ob_button_add.setCurrentText("Такая запись уже существует")
		else:
			self.__ob_button_add.setCurrentText("Назад")