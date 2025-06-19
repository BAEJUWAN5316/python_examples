# chat/views.py

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from chat.models import PuzzleRoom


# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능
# @app.get("/chat/") > fast api 스타일!


# 채팅 기본 화면을 보여주겠습니다
def index(request: HttpRequest) -> HttpResponse:

    # html_str = "<html><head></head><body><h1>hello django in html</h1></body>"

    # # return HttpResponse("hello django") # text/html 기본은 html로 응답!
    # return HttpResponse(html_str)

    return render(request, "chat/index.html")  # 여기에는 html말고 여러가지 넣을 수 있다
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
    request.GET  # queryDit타입(Dict로 보여도 90%무방) > post 요청에서도 있을 수 있어요
    request.POST  # POST데이터 (queryDict)

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
def puzzleroom_play(request: HttpRequest, id: int) -> HttpResponse:

    room = PuzzleRoom.objects.get(id=id)
    image_url = room.image_file.url
    level = room.level

    return render(
        request,
        template_name="chat/puzzle.html",
        context={"image_url": image_url, "level": level},
    )


def puzzleroom_list(request):
    # puzzle room 테이블에 있는 모든 레코드를 가져올 준비
    qs = PuzzleRoom.objects.all()
    return render(
        request,
        template_name="chat/puzzleroom_list.html",
        context={"puzzleroom_list": qs},
    )


# import코드는 최상단에 원래 써주세요!
from chat.forms import PuzzleRoomForm

# 1개의 puzzleroo 생성을 위해 2번의 요청을 받을 예정
# 1> 빈 입력 서식을 보여줘야 합니다.
# 2> 유저가 서식에 값을 채우고 전송(저장) 버튼을 눌렀을 때, 
# 유저의 입력값을 전송합니다 (반복)
def puzzleroom_new(request: HttpRequest) -> HttpResponse:
    # 1> 빈 입력 서식을 보여주겠습니다.

    if request.method == "GET": # "GET" or "POST" 뿐
        form = PuzzleRoomForm()

    else: # "POST" : 유저가 입력한 값에 대한 유효성 검사, 통과되면 저장, 실패면 에러응답
        request.POST # POST 요청에서의 데이터(파일 제외) > 파일 제외 모두
        request.FILES # POST 요청에서의 데이터(파일 만) > 유저가 올린 파일

        # Form에게 유저의 모든 입력 데이터를 전달
        form = PuzzleRoomForm(data=request.POST, files=request.FILES )
        # form : 유저가 전달한 값을 모두 알고 있습니다.
        # 입력 필드 구성도 모두 알고있습니다.

        # 단 1개의 유효성 검사라도 실패하면, False 반환, 모두 통과하면 True 반환
        if form.is_valid(): # 호출 즉시 유효성 검사를 수행합니다
            form.save() # 유저가 입력한 값을 데이터베이스에 저장합니다(ModelForm의 기능)
            return redirect("/chat/puzzle/") #django.shortcuts import에 redircet 추가
        else:
            pass #에러나면 아래로 그냥 진행 아래에서 에러 출력기능도 어차피 있음

    # 장고의 문화대로, 파일명과 view 이름을 쓰고 있습니다
    return render(request, "chat/puzzleroom_form.html", {
        "form": form,
    })