from fastapi import FastAPI,Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

items = {}

#고정된 틀 만들기

class Item(BaseModel):
    name: str #이건 필수값이 된다!
    description: Optional[str] = None #descriotion은 빈 값이 들어가도 된다 라는 뜻
    price: float


class ItemUpdate(BaseModel): #업데이트 할 때의 틀 설정
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

@app.post("/items/{item_id}", response_model=Item) #Item이라는 클래스를 반영해서 반환하겠다고 지정해주는 것, 반환값을 제한
def create_item(item_id: int, item: Item): # 여긴 입력값의 틀을 제한
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists") #강제로 에러를 터트리는 것 일부러 예외를 발생시켜버리는 것
    # 200: 성공, 400: 서버 처리 불가, 404: 찾을 수 없음
    # 에러는 메모리부족 등으로 처리할 수 없는 거
    # 예외는 우리가 방지 할 수 있는 것
    # 결론은 예외는 컨트롤 할 수 있는 것, 에러는 할 수 없는 것
    items[item_id] = item
    return item

@app.get("/items", response_model=List[Item]) # item만 들어있는 리스트를 반환하겠다는 뜻
def read_items():
    return list(items.values())

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id:int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

# @app.get("/itemss")
# def read_items():
#     return list(items.items())
# 키값까지 확인하려면 이렇게!

@app.get("/items-keys", response_model=List[int])
def read_keys():
    return list(items.keys())

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item:ItemUpdate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    stored_item: Item = items[item_id]
    update_data = item.model_dump(exclude_unset=True)
    # update_data = item.dict
    # 글자에 줄이 그이면 쓸 수는 있지만 권장되지 않음! 이라는 뜻
    # 더 좋은 기능이 있으니까 그거 쓰라! 라는 뜻
    # model_dump는 딕셔너리로 만들어주는 메서드
    # exclude_unset은 True인 값만 딕셔너리로 만들어주겠다! 라는 뜻
    
    updated_item = stored_item.model_copy(update=update_data)
