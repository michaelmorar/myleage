from data.filex.file import File
from data.db.mongo.mongopy import MongoPy
import yaml

class Mileage:

	def __init__(self, date, miles, config_file_string):
		self.date = date
		self.miles = miles
		config_file = 'config/local_mileage_conf.yaml' if config_file_string == None else config_file_string
		yf = open(config_file, 'r')
		self.parsedYaml = yaml.load(yf)
		#print(self.parsedYaml)

	def log(self, output_type):
        	# Log the mileage :w:x

		if output_type == "file":
			f1 = File("C:/stuff", "mileage.txt")
			f1.write()

		if output_type == "mongo":
			py = self.parsedYaml
			m1 = MongoPy(py.get('mongoDB-string'), py.get('mongoDB-database'), py.get('mongoDB-collection'), py.get('protocol'))
			#todo  - inject credentials if they exist - py.get('mongoDB-user'), py.get('mongoDB-password')

			if (py.get('mongoDB-user')):
				m1.set_user(py.get('mongoDB-user'))
			if (py.get('mongoDB-password')):
				m1.set_password(py.get('mongoDB-password'))


			m1.connect()
			m1.insert(self.date, self.miles)

	def get_mongo_connection(self):
		py = self.parsedYaml
		return (py.get('protocol')+py.get('mongoDB-user')+":"+py.get('mongoDB-password')+'@'+py.get('mongoDB-string'))