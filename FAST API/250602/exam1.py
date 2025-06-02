from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Optional, List

app = FastAPI()

users = {}

class User(BaseModel):
    name : str
    age : int
    phone : Optional[int] = None
    active : bool = True

class UserUpdate(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    phone : Optional[int] = None


@app.get("/users", response_model=List[User])
def get_users():
    return list(users.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="찾을 수 없는 유저 아이디 입니다.")
    return users[user_id]

@app.post("/users/{user_id}", response_model=User)
def create_user(user_id: int, user: User):
    if user_id in users:
        raise HTTPException(status_code=404, detail="이미 존재하는 ID입니다.")
    users[user_id] = user
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_up: UserUpdate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="찾을 수 없는 유저 아이디 입니다.")
    user_data: User = users[user_id]
    update_data = user_up.model_dump(exclude_unset=True)
    updated_data = user_data.model_copy(update=update_data)
    users[user_id] = updated_data
    return updated_data

@app.put("/users/{user_id}/active")
def deactive_user(user_id: int, state: bool):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="찾을 수 없는 유저 아이디 입니다.")
    user_act:User = users[user_id]

    if user_act.active == state:
        raise HTTPException(status_code=400, detail="이미 비활성화 또는 활성화 상태입니다.")
    user_act.active = state
    return user_act