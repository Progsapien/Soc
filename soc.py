
class Soc:
	def __init__(self):
		self.__title = 0
		self.__text = 0

	@property
	def title(self):
		return self.__title

	@property
	def text(self):
		return self._text

	@title.setter
	def title(self, value):
		if(type(value) == str and not str(value).isdigit()):
			self.__title = str(value)

	@text.setter
	def text(self, value):
		if(type(value) == str and not str(value).isdigit()):
			self.__text = str(value)
	
	