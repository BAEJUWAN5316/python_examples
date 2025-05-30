from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
blogs = ["블로그1번","블로그2번","블로그3번", "4번"]

@app.get("/blog/{post_id}") #blog/1 blog/2 이런 식으로 뒤에 들어가는 숫자를 동적으로 두는 것!
def blog_detail(post_id: int): # 어쩌고: int 라는 뜻은 어쩌고가 int 여야한다고 지정해주는 것!! 형변환과는 다름
    return {"게시물 번호": post_id}

@app.get("/blog/{post_tag}/{post_author}")
def tag_author_list(post_tag: str, post_author: str):
    return {"태그":post_tag, "저자":post_author}

@app.get("/")
def index():
    return {"인사말":"반갑습니다"}

@app.get("/blog")
def blog_list():
    return {"블로그 목록":blogs}

@app.get("/blog/{post_tag}")
def tag_list(post_tag: str):

    b = []
    for blog in blogs:
        if post_tag in blog:
            b.append(blog)
    
    return {"블로그(태그) 목록" : b}

@app.get("/hello/{name}")
def get_name(name:str):
    return {name:"반갑습니다~"}

@app.get("/calculate/{operation}/{a}/{b}")
def get_name(operation: str, a: int, b: int):
    if operation == "add":
        return {f"add {a} + {b}" : a + b}
    elif operation == "subtract":
        return {f"subtract {a} - {b}" : a - b}
    elif operation == "multiply":
        return {f"multiply {a} * {b}" : a * b}
    elif operation == "divide":
        return {f"divide {a} / {b}" : a / b}



