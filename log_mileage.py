from mileage import Mileage
import sys

conf = None if not sys.argv[1] else sys.argv[1]

m1 = Mileage("2019-03-21", 5000, conf)

#print(m1.date, m1.miles)
m1.log("file")
m1.log("mongo")



