# chat/views.py

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
# @app.get("/chat/") > fast api 스타일!

# 채팅 기본 화면을 보여주겠습니다
def index(request: HttpRequest) -> HttpResponse:

    # html_str = "<html><head></head><body><h1>hello django in html</h1></body>"

    # # return HttpResponse("hello django") # text/html 기본은 html로 응답!
    # return HttpResponse(html_str)

    return render(request, "chat/index.html") # 여기에는 html말고 여러가지 넣을 수 있다
    # 장고 앱에서는 앱/templates 폴더 아래에 템플릿 파일을 두면,
    # ( 이때 해당 앱은 settings.INSTALLED_APPS 에 필히 등록된 상태 )
    # render 시에 장고가 알아서 그 파일을 찾아줍니다.
    # render 호출 시에는 templates/ 하위 경로명을 지정합니다.

# 매 채팅메세지를 받아 응답 메세지를 만들고, 응답하겠어요
# HTTP Methods : get, post, put, delete, patch, options
# http : 웹페이지, 웹문서를 위한 프로토콜
# <form> 태그(유저로부터 입력을 받아 지정 서버로 전송)에서는 get, post만 지원
# get : 조회 목적 > 요청해도 데이터는 변하지 않는다/안전하다 > 검색엔진은 항상 get 요청
# post : 파괴적인 액션 (추가/수정/삭제 등)
# 조회목적인데 post 요청을 하는 서비스가 있어요
# JS API를 통해서 put, patch, delete 등의 요청을 할 수 있어요
def chat_message_new(request: HttpRequest) -> HttpResponse:
    # query parameters
    request.GET # queryDit타입(Dict로 보여도 90%무방) > post 요청에서도 있을 수 있어요
    request.POST # POST데이터 (queryDict)

    question = request.POST.get("question", "")
    if question:
        answer = f"당신의 질문 : {question}"
    else:
        answer = "질문이 없으시네요"
    return HttpResponse(answer)
