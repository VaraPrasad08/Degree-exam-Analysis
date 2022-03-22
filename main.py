from http import client
import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=client['Employee']
information=mydb.information

records=[
    {
    'firstname':'vara',
    'lastname':'prasad',
    'department':'INFORMATION TECHNOLOGY'
},
{
    'firstname':'s',
    'lastname':'deepika',
    'department':'INFORMATION TECHNOLOGY'
},
{
    'firstname':'surya',
    'lastname':'teja',
    'department':'INFORMATION TECHNOLOGY'
},{
    'firstname':'veera',
    'lastname':'manikanta',
    'department':'INFORMATION TECHNOLOGY'}]

x=information.insert_many(records)
print(x.inserted_ids)