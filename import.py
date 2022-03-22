import pandas as pd
from pandas import DataFrame
import pymongo
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
client = pymongo.MongoClient('mongodb://localhost:27017/')


db = client.StudentData
data=pd.read_csv('Student.csv')

class student(BaseModel):
    writing_score:str=None
    test_preparation_course:str=None
    reading_score:str=None
    race_and_enthnicity: str=None
    parent_level_of_education:str=None
    math_score:str=None
    lunch:str=None
    gender:str=None

@app.get("/", response_description="List all students")
def list_students():
    users = []
    for user in db["information"] .find():
        users.append(student(**user))
        
        
    return {'users': users,"data":data}
@app.get("/rank")
def rank():
    df = DataFrame (list(db.information.find({})))
    return df
