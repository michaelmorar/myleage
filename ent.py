from mileage import Mileage

m1 = Mileage("2019-03-21", 5000)

print(m1.date, m1.miles)
m1.log("file")
m1.log("mongo")



