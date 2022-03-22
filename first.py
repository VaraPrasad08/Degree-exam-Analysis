import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from bson import ObjectId
from typing import Optional
import pymongo


app = FastAPI()
#Connecting to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.college

#The _id Attribute and ObjectIds
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

#Database Models
class StudentModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: any = Field(...)
    email: EmailStr = Field(...)
    address: str=Field(...)
    mobile_number:int=Field(...)
    country:str=Field(...)
    state:str=Field(...)
    Zip:int=Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "address": "main road,kkd",
                "mobile_number": 9959469892,
                "country":"India",
                "state":"Andhra Pradesh",
                "Zip":533101,
            }
        }


class UpdateStudentModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    address: Optional[str]
    mobile_number: Optional[int]
    country:Optional[str]
    state:Optional[str]
    Zip:Optional[int]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "address": "main road,kkd",
                "mobile_number": 9959469892,
                "country":"India",
                "state":"Andhra Pradesh",
                "Zip":533101,
            }
        }


 
@app.post("/", response_description="Add new student", response_model=StudentModel)
async def create_student(student: StudentModel = Body(...)):
    student = jsonable_encoder(student)
    new_student =db["students"].insert_one(student)
    created_student = db["students"].find_one({"_id": new_student.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)



@app.get("/", response_description="List all students")
def list_students():
    users = []
    for user in db["students"]  .find():
        users.append(StudentModel(**user))
    return {'users': users}



@app.get(
    "/{id}", response_description="Get a single student", response_model=StudentModel
)
async def show_student(id: str):
    if (student := db["students"].find_one({"_id": id})) is not None:
        return student
    raise HTTPException(status_code=404, detail=f"Student {id} not found")



@app.put("/{id}", response_description="Update a student", response_model=StudentModel)
async def update_student(id: str, student: UpdateStudentModel = Body(...)):
    student = {k: v for k, v in student.dict().items() if v is not None}
    if len(student) >= 1:
        update_result =  db["students"].update_one({"_id": id}, {"$set": student})
        if update_result.modified_count == 1:
            if (
                updated_student := db["students"].find_one({"_id": id})
            ) is not None:
                return updated_student
    if (existing_student := db["students"].find_one({"_id": id})) is not None:
        return existing_student
    raise HTTPException(status_code=404, detail=f"Student {id} not found")

@app.delete("/{id}", response_description="Delete a student")
async def delete_student(id: str):
    delete_result = db["students"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Student {id} not found")