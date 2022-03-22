from fastapi import FastAPI
from new import student
import connection as conn

onlineemxamlist=conn.db['students']
app=FastAPI()

@app.get("/ssc")
def find():
    users = []
    for user in onlineemxamlist.find():
        users.append(student(**user))
    return{"data":users}


@app.post("/", response_description="Add new student", response_model=student)
async def create_student(student: student ):
    new_student =onlineemxamlist.insert_one(student)
    created_student = onlineemxamlist.find_one({"_id": new_student.inserted_id})
    return {'content':created_student}