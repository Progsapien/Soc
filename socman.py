from soc import Soc
from pickle import load, dump

class SocMan:
	def __init__(self):
		self.__lib = []
		try:
			file = open("soc","rb")
			self.__lib = load(file)
			file.close()
		except:
			pass

	def add(self, title, text):
		item = Soc()
		if(not item.setText(text) and not item.setTitle(title)):
			self.__lib.append(item)
			self.save()
			return 0
		else:
			return -1

	def delete(self, item):
		if(type(item) == Soc):
			self.__lib.remove(item)
			self.save()
			return 0
		else:
			return -1

	def save(self):
		file = open("soc","wb")
		dump(self.__lib, file)
		file.close()

	def getDump(self):
		return self.__lib

	def search(self, value):
		founded = []
		if(type(value) == str):
			for item in self.__lib:
				if(value in item.getTitle()):
					founded.append(item)
		return founded

