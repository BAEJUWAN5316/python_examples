from fastapi import FastAPI
from pydantic import BaseModel

# 가영문제 2

app = FastAPI()

users = []

class Info(BaseModel):
    name : str
    age : int = 0

@app.get("/")
def users_list():
    return users

@app.post("/users")
def add_user(user : Info):
    users.append(user)
    return {"message" : f"{user.name}님, 등록이 완료되었습니다."}

