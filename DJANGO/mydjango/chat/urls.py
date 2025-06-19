# chat/urls.py 파일 생성
from django.urls import path
from . import views

urlpatterns = [
    # 아래에서 곧 구현합니다.
    # 이 코드를 저장하시면 개발서버에서 index 함수를 찾지못해 오류가 발생할 것이지만,
    # 아래 chat/views.py 저장 후에는 해당 오류가 사라질 것입니다.
    path("", views.index),
    path("messages/new/", views.chat_message_new),
    path("puzzle/", views.puzzleroom_list),
    # puzzle/ 주소에 문자열 패턴이 있고, 뒤에 /가 있으면
    # /chat/puzzle/{name}/
    # 아래에서 str은 정규표현식이다
    # 가급적 이 정규표현식은 타이트하게 호출 가능하게만 지정하도록 추천
    # path("puzzle/<str:name>/", views.puzzleroom_play),  
    path("puzzle/<int:id>/", views.puzzleroom_play),  # 토이스토리 부분
    # 지금은 숫자만 받을 거니 int로 가자
]
