from fastapi import FastAPI
import pandas as pd
from typing import Optional
from pydantic import Field,BaseModel
import pymongo
import json
client = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = client["Data"]
mycol = mydb["information"]
x=mycol.find_one()
app=FastAPI()
class Student(BaseModel):
    
    examName:str=Field(...)
    examStartDateTime:datetime=Field(...)
    examEndDateTime:datetime=Field(...)
    randomQue:str=Field(...)
    randomAns:str=Field(...)
    repeatable:str=Field(...)
    displayResult:str=Field(...)
    duration:str=Field(...)
    status:str=Field(...)
    papercode:str=Field(...)
    ipAddress:str=Field(...)
    userId:str=Field(...)
    schema:str=Field(...)
    programId:str=Field(...)
    programName:str=Field(...)
    ExamID:str=Field(...)
    object:str=Field(...)
    class Config:
        schema={
            "example":{
                'examName':"NEW EXAM APP",
                'examStartDateTime':'2021-06-13T18:30:00.000+00:00',
                'examEndDateTime':'2021-06-18T18:29:00.000+00:00',
                'randomQue':'1',
                'randomAns':'0',
                'repeatable':'0',
                'displayResult':'1',
                'duration':'180',
                'status':'1',
                'papercode':'210420131126807',
                'ipAddress':'****',
                'userId':'11',
                'schema':'JEEMAINS_2021',
                'programId':'2',
                'programName':'JEE MAINS',
                'ExamID':'24182',
                "object":[{
                    'groupName':'MYDEMO',
                    'groupID':262
                }]
            }
        }

class UpdateStudent(BaseModel):
    examName:Optional[str]
    examStartDateTime:Optional[datetime]
    examEndDateTime:Optional[datetime]
    randomAns:Optional[str]
    repeatable:Optional[str]
    displayResult:Optional[str]
    duration:Optional[str]
    status:Optional[str]
    papercode:Optional[str]
    ipAddress:Optional[str]
    userId:Optional[str]
    schema:Optional[str]
    programId:Optional[str]
    programName:Optional[str]
    ExamID:Optional[str]
    object:Optional[str]

    class Config:
        schema= {
            "example": {
                'examName':"NEW EXAM APP",
                'examStartDateTime':'2021-06-13T18:30:00.000+00:00',
                'examEndDateTime':'2021-06-18T18:29:00.000+00:00',
                'randomQue':'1',
                'randomAns':'0',
                'repeatable':'0',
                'displayResult':'1',
                'duration':'180',
                'status':'1',
                'papercode':'210420131126807',
                'ipAddress':'****',
                'userId':'11',
                'schema':'JEEMAINS_2021',
                'programId':'2',
                'programName':'JEE MAINS',
                'ExamID':'24182',
                "object":[
                {
                        'groupName':'MYDEMO',
                        'groupID':262
                }]
            }
        }

@app.get("/")
def find():
    users = []
    for user in mycol.find():
        users.append(Student(**user))
    return {'users': users}