from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()


items = []

class Item(BaseModel):
    name: str
    price: float = 0  #기본값은 0으로 주겠다는 뜻


@app.get("/item")
def item_list():
    return {"item":items}

'''
@app.post("/item/create")
def create_item(item: dict):
    items.append(item)
    return {"item": item}
'''

# 썬더 머시기에서 body 누르고 JSON란에 {"name": "item1","price": 100} 이거 넣고
# send누르면 웹페이지 창에서 리스트에 어펜드 된 걸 볼 수 있다!

@app.post("/item/create")
def create_item(item: Item):  # 타입힌팅을 Item으로 바꿔준다! 그럼 요청값이 클래스 Item에서 지정해준 거랑 같아야함!
    items.append(item)
    print(item.name, item.price)
    return {"item": item}

@app.put("/item/{item_id}")
def item_update(item_id: int, item: Item):
    items[item_id - 1] = item
    return {"item": item}




class Person(BaseModel):
    name: str
    email: str
    age: int

people = []

@app.post("/people")  # get, post 가 다르면 엔드포인트가 같아도 된다! get으로 조회된다!
def create_people(person: Person):
    people.append(person)
    return {"등록된 유저": person}

@app.get("/people")
def people_list():
    return {"유저리스트": people}

@app.get("/people/{list1}")
def get_list(list1: int):
    return {"person": people[list1-1]}

@app.delete("/people/{person_id}")
def delete_user(person_id: int):
    del people[person_id-1]


