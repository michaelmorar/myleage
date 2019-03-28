import pymongo

class MongoPy:

	def __init__(self, string, database, collection, protocol):
		self.string = string
		self.database_name = database
		self.collection_name = collection
		self.user = ""
		self.password = ""
		self.protocol = protocol

	def connect(self):
		connection_string = self.assemble_connection_string()
		print(connection_string)
		client = pymongo.MongoClient(connection_string)
		self.mydb = client[self.database_name]
		self.collection = self.mydb[self.collection_name]
		print(self.collection)

	def insert(self, in_date, in_miles):
		mydict = { "date": in_date, "miles": in_miles }
		x = self.collection.insert_one(mydict)

	def assemble_connection_string(self):
		return (self.protocol + "://" + ((self.user + ":") if self.user else "" ) + ((self.password + "@") if self.password else "" )  + self.string) 

	def find_one(self):
		print(self.collection.find_one())

	def set_user(self, user):
		self.user = user

	def set_password(self, password):
		self.password = password