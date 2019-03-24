class File:

	def __init__(self, path, name):
		self.path = path
		self.name = name


	def write(self):
		print (self.path, self.name)
