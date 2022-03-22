
from fastapi import FastAPI
import connection
from bson import ObjectId
from pydantic import BaseModel, EmailStr,Field

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

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email :EmailStr=None
    name :str=None
    password :str=None

# An instance of class User
newuser = User()

# funtion to create and assign values to the instanse of class User created
def create_user(email, username, password):
    newuser.id = ObjectId()
    newuser.email = email
    newuser.name = username
    newuser.password = password
    return dict(newuser)

# A method to check if the email parameter exists from the users database before validation of details
def email_exists(email):
    user_exist = True

    # counts the number of times the email exists, if it equals 0 it means the email doesn't exist in the database
    if connection.db.users.find(
        {'email': email}
    ).count() == 0:
        user_exist = False
        return user_exist

# Reads user details from database and ready for validation
def check_login_creds(email, password):
    if not email_exists(email):
        activeuser = connection.db.users.find(
            {'email': email}
        )
        for actuser in activeuser:
            actuser = dict(actuser)
            # Converted the user ObjectId to str! so this can be stored into a session(how login works)
            actuser['_id'] = str(actuser['_id'])    
            return actuser


app = FastAPI()


# Our root endpoint
@app.get("/")
def index():
    return {"message": "Hello World"}


# Signup endpoint with the POST method
@app.post("/signup/{email}/{username}/{password}")
def signup(email, username: str, password: str):
    user_exists = False
    data = create_user(email, username, password)

    # Covert data to dict so it can be easily inserted to MongoDB
    dict(data)

    # Checks if an email exists from the collection of users
    if connection.db.users.find(
        {'email': data['email']}
        ).count() > 0:
        user_exists = True
        print("User Exists")
        return {"message":"User Exists"}
    # If the email doesn't exist, create the user
    elif user_exists == False:
        connection.db.users.insert_one(data)
        return {"message":"User Created","email": data['email'], "name": data['name'], "pass": data['password']}

# Login endpoint
@app.get("/login/{email}/{password}")
def login(email, password):
    def log_user_in(creds):
        if creds['email'] == email and creds['password'] == password:
            return {"message": creds['name'] + ' successfully logged in'}
        else:
            return {"message":"Invalid credentials!!"}
    # Read email from database to validate if user exists and checks if password matches
    logger = check_login_creds(email, password)
    if bool(logger) != True:
        if logger == None:
            logger = "Invalid Email"
            return {"message":logger}
    else:
        status = log_user_in(logger)
        return {"Info":status}