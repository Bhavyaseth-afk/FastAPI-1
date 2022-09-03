from typing import List
from fastapi import FastAPI,HTTPException

from models import Gender, Roles, User


app = FastAPI()

db:List[User]= [
    User(id=2, first_name="jj",last_name="ff",gender=Gender.female,roles=[Roles.student]),    
    User(id=3, first_name="vv",last_name="yy",gender=Gender.male,roles=[Roles.admin,Roles.user])

]

@app.get("/")
async def root():
    return {"bhavya":"world"}

@app.get("/api/user")
async def fetch_users():
    return db 

@app.post("/api/user")
async def register(user:User):
    db.append(user)
    return {"id":user.id}

@app.delete("/api/user/{user_id}")
async def user_del(user_id:int):
    for u in db:
        if u.id==user_id:
            db.remove(u)
            return db
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} dosent exist"
    )
        
    