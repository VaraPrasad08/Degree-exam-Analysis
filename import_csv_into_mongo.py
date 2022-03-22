import pymongo
import pandas as pd
client = pymongo.MongoClient('mongodb://localhost:27017/')

db=client.StudentData

df=pd.read_csv('Student.csv')
data=df.to_dict(orient='records')
db.information.insert_many(data)
print(data)