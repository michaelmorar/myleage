import pymongo

client = pymongo.MongoClient("mongodb+srv://ares_it_1:SE44HNdYcCxP22B@cluster0-m9ejp.mongodb.net/test?retryWrites=true")
mydb = client["db_mileage"]

mycoll = mydb["mileages"]

x = mycoll.find_one()

#print(x)

mydict = { "date": "2019-03-19", "mileage": 8001 }

#x = mycol.insert_one(mydict)

myquery = { "date": "2019-03-19" }

mydoc = mycoll.find(myquery)

for x in mydoc:
  print(x)







