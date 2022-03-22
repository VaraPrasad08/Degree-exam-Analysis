import os
from xml.sax.handler import feature_namespace_prefixes
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import pymongo

app = FastAPI()
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.college
mycol=db.data


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class student(BaseModel):
    id: Optional[PyObjectId]= Field( alias="_id")
    name: str= Field(...)
    gender:str= Field(...)
    age:int=Field(..., le=100)


    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
 
@app.post("/", response_model=student)
def Create_details(student: student):
    students = jsonable_encoder(student)
    if hasattr (students, 'id'):
        delattr(students, 'id')
    new_student =mycol.insert_one(students.dict(by_alias=True))
    students.id= new_student.inserted_id
    return {"user":students}

@app.get("/", response_description="List all students")
async def list_details():
    users = []
    for user in mycol.find():
        users.append(student(**user))
    return {'users': users}

@app.delete("/{id}", response_description="Delete a student", response_model=student)
async def delete_data(id: str):
    delete_result = mycol.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Student {id} not found")