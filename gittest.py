from typing import Union
#1/2/26
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

my_database = {}

class Profile(BaseModel):  
    name: str
    age: int
    address: str
    id: int

@app.post("/create-profile/{user_id}")#here checks the user_id
def create(user_id: int, data: Profile):
    my_database[id] = user_id
    profile_data = my_database[id]#this is the display for user id if its setted
    return{"message": "Success", "user_id": profile_data}#here

@app.get("/check-profile/{user_id}") #heres the view
def view(user_id: int):
    if user_id not in my_database:
        return{"error": "invalid user", "message": "missmatched"}
    else:
        return{"user": "found", "user": "matched"}

@app.put("/update-profile/{user_id}") #so this is update
def update(user_id: int, data: Profile):
    my_database[user_id] = data
    return {"message": "Profile Updated!"}

@app.get("/update-profile/{user_id}") #this is view
def update(user_id: int, data: Profile):
    if user_id not in my_database:
        return{"user_id": "error", "format": "invalid"}
    else:
        {"user_id": "found"}




