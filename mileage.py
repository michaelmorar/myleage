from data.filex.file import File
from data.db.mongo.mongopy import MongoPy
import yaml

class Mileage:

	def __init__(self, date, miles):
		self.date = date
		self.miles = miles
		config_file = open('config/mileage_conf.yaml','r')
		self.parsedYaml = yaml.load(config_file)
		print(self.parsedYaml)

	def log(self, output_type):
        	# Log the mileage 
		print(self.date, self.miles)
		if output_type == "file":
			f1 = File("C:/stuff", "mileage.txt")
			f1.write()

		if output_type == "mongo":
			print(self.get_mongo_connection())
			m1 = MongoPy()

	def get_mongo_connection(self):
		py = self.parsedYaml
		return ("mongodb+srv://"+py.get('mongoDB-user')+":"+py.get('mongoDB-password')+'@'+py.get('mongoDB-string'))


