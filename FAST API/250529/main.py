from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

notice1 = ["공지사항1","공지사항2","공지사항3"]
# 127.0.0.1:8000 이라는 건 웹상에서 '나'를 뜻함!

templates = Jinja2Templates(directory="templates")
# 구동중인 폴더에 templates라는 폴더를 보겠다! 라는 뜻! > 만들어줘야함 폴더를

@app.get("/") # 127.0.0.1:8000 get method
def read_root():
    return {"Hello":"World"}

@app.get("/about") # 127.0.0.1:8000/about get method
def about():
    return {"message":"about page"}

@app.get("/contact") # 127.0.0.1:8000/contact get method
def contact():
    return {"message":"contact page"}

@app.get("/notice") # 127.0.0.1:8000/notice get method
def notice():
    return {"notice": notice1}

@app.post("/")
def post_root():
    return {"이건":"포스트입니다."}

@app.get("/good")
def read_goo():
    return {"a": 1}

@app.get("/users/get")
def get_users():
    return {"a":1, "b":2}

@app.get("/todo")
def get_todo():
    return {"todo반환":"반환"}

@app.get("/login")
def get_login():
    return ["로","그인"]

@app.get("/info")
def get_info():
    return {"이름":"max", "주소":{"zipcode":12345,"주소1":"서울특별시","주소2":"505호"}}

# HTML클래스로 응답해주겠다는 선언!
# 기본 응답값은 JSON이다!
@app.get("/index", response_class=HTMLResponse)
def index():
    return '<h1> 너무 더워요</h1>'

@app.get("/index2") # 127.0.0.1:8000/index2 get method
def index2(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})



