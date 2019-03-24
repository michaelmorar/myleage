import pymongo

class MongoPy:

	def __init__(self, string, user, password, database, collection):
		self.string = string
		self.user = user
		self.password = password
		self.database_name = database_name
		self.collection_name = collection_name

	def connect(self):
		connection_string = assemble_connection_string()
		client = pymongo.MongoClient(connection_string)
		self.mydb = client[self.database_name]
		self.collection = mydb[self.collection_name]

	#def write(self):

	def assemble_connection_string(self):
		return ("mongodb+srv://" + self.user + ":" + self.password + "@" + string) 

	def find_one():
		print(self.collection.find_one())






