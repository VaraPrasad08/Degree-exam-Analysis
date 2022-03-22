import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['college']
print("database connection is sucessfull")