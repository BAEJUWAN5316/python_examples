# chat/views.py

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from chat.models import PuzzleRoom


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

# chat/views.py
# 다양하게 올 name인자를 받아줘야한다
# 없는 데이터를 요청했는데 500서버로 나오면 억울함!
# 404로 응답이 오는게 맞다
def puzzle_room(request, name):
    # image_url/level 설정을 view단에 하드코딩 하는게 아니라
    # 유저가 이미지와 레벨을 설정해서 게임방을 만들 수 있으면 좋겠다!
    # > 이러한 건 보통은 데이터베이스에 저장/수정하고 불러서 활용합니다.
    # 보통의 애플리케이션들은 대개 데이터베이스 중심의 소프트웨어입니다

    try:
        image_url = {
                "mario": "/static/chat/mario.jpg",
                "toy": "/static/chat/toy-story.jpg",
                "openai-1": "/static/chat/openai-1.png",
            }[name]
    except KeyError:
        # from Http404부분 해줘야한다!
        raise Http404(f"not found room : {name}")
    
    level = 3 # or 4, 5


    # name에 올 toy, mario, game... 등등
    # 반드시 toy만 오는게 아니기 때문에 신뢰 해서는 안된다
    # 항사 우리가 원하는 규칙에 맞는지 검사해야합니다
    return render(request, 
                template_name="chat/puzzle.html", 
                context={ "image_url": image_url, "level": level })

def puzzleroom_list(request):
    # puzzle room 테이블에 있는 모든 레코드를 가져올 준비
    qs = PuzzleRoom.objects.all()
    return render(request, 
                template_name="chat/puzzleroom_list.html",
                context={ "puzzleroom_list":qs })
