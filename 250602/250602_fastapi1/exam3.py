from fastapi import FastAPI
from pydantic import BaseModel

# 가영문제 3

app = FastAPI()

users = [
    {"name": "홍길동", "age": 25},
    {"name": "이영희", "age": 32},
    {"name": "김민수", "age": 40}
]

@app.get("/")
def users_list():
    return users

@app.get("/users")
def filter_user(min_age : int = 0):
    fuser = list(filter(lambda x : x["age"] >= min_age ,users))
    return fuser
    

