
class Soc:
	def __init__(self):
		self.__title = 0
		self.__text = 0

	def getTitle(self):
		return self.__title

	def getText(self):
		return self.__text

	def setTitle(self, value):
		if(type(value) == str and not str(value).isdigit()):
			self.__title = str(value)
			return 0
		else:
			return -1

	def setText(self, value):
		if(type(value) == str and not str(value).isdigit()):
			self.__text = str(value)
			return 0
		else:
			return -1
	
	