from mileage import Mileage
import sys
# forcing changes 


if len(sys.argv) >= 3:
	conf = None if not sys.argv[1] else sys.argv[1]
	date = sys.argv[2]
	miles = sys.argv[3]
else: 
	date = "1979-01-01"
	miles = 1
	print("Defaulting arguments")
	conf = None

m1 = Mileage(date, miles, conf)


#print(m1.date, m1.miles)
m1.log("file")
m1.log("mongo")



