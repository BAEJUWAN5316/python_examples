from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 은빈 문제1
# @app.get("/")
# def get_user():
#     return users

# @app.post("/user/{user_id}")
# def create_user(user_id : int, user : User):
#     for names in users.values():
#         if names.name == user.name:
#             raise HTTPException(status_code=400, detail="이미 존재하는 이름입니다.")

#     if 1<= 2025 - user.birth_year - 7 <= 6:
#         users[user_id] = user
#         return user
#     elif 2025 - user.birth_year > 6:
#         return "졸업"
#     elif 2025 - user.birth_year < 1:
#         return "입학 전"


# 은빈 문제 2

users = {
    "admin": {"password": "admin123"},
    "guest": {"password": "guest@2024"}
}

@app.post("/user")
def find_users(username: str, password: str):
    username = 


    if username not in users:
        raise HTTPException(status_code=404, detail="id was not exist")
    
    if username[]password != users[username]["password"]:
        raise HTTPException(status_code=401, detail="password was wrong")
    
    return {"message": "Welcome, admin!"}
