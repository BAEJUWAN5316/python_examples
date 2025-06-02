from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 간단한 데이터 저장소
messages = []

@app.get("/", response_class=HTMLResponse) #내가 반환하는 값은 HTML이야 라는 뜻
def home(request: Request): # request: Request 이게 있어야 jinj2가 작동한다!
    # 메인 페이지- 데이터를 탬플릿에 전달
    context = {
        "request": request,           # 필수! 빠지면 안 동작한다!
        "title": "안녕하세요!",         #키값에 맞는 밸류값으로 html에 있는 파일에 {{ }}에 있는 값으로 변한다!
        "message_count": len(messages),
        "messages": messages
    }
    return templates.TemplateResponse("home.html", context)

@app.get("/write", response_class=HTMLResponse)
def write_form(request: Request):
    """글쓰기 폼 페이지"""
    context = {
        "request": request,
        "title": "메시지 작성"
    }
    return templates.TemplateResponse("form.html", context)
    
@app.post("/write", response_class=HTMLResponse)
def write_message(request:Request, name:str = Form(...), message:str = Form(...)): #...이건 반드시 입력값이 필요하단 뜻!
    """폼 데이터 받아서 처리"""
    # 새 메시지 저장
    new_message = {"name": name, "message": message}
    messages.append(new_message)
        # 결과 페이지 보여주기
    context = {
        "request": request,
        "title": "작성 완료",
        "name": name,
        "message": message
    }
    return templates.TemplateResponse("result.html", context)



