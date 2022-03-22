import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = client["Employee"]
mycol = mydb["information"]

for x in mycol.find({},{'firstname':1}):
    print(x)

