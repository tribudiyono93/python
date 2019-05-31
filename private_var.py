class Map:
	def __init__(self, iterate):
		self.list = []
		self.__geek(iterate)
	def geek(self, iterate):
		for item in iterate:
			self.list.append(item)
	__geek = geek

class MapSubClass(Map):
	def geek(self, key, value):
		for i in zip(keys, values):
			self.list.append(i)