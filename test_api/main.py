from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
 
 
app = FastAPI()

user1 = Jinja2Templates(directory="dragon")
 
@app.get("/")
def read_root():
   return {"Hello": "Worldㅇㅇ"}


@app.get("/hello")
def get_hello():
   return {"반가워요":"여러분"}

@app.get("/index", response_class=HTMLResponse)
def index():
   return "<h1>방가방가루~</h1>"

@app.get("/index2") # -> 127.0.0.1:8000/index2 get method
def index2(request: Request):
    return user1.TemplateResponse("fufu.html", {"request": request})