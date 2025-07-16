import json
from django.db.models.functions import Length
from django.http import HttpResponse
from django.urls import path
from melon.models import Song, Todo
from melon.api.serializers import SongSerializer, TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet


# FBV 버전의 DRF API
# @api_view(["GET"])
# def song_list(request):
#     # Database Function을 호출해서, title 길이 계산을 요청.
#     qs = Song.objects.all()
#     qs = qs.annotate(title_length=Length("title"))

#     # 데이터 변환의 기능을 제공(시리얼라이저 오리지널 기능)
#     #  입력 데이터에 대한 유효성 감사 및 저장(FORM의 기능)
#     serializer = SongSerializer(
#         instance=qs,
#         many=True,
#     )
#     song_list_data = serializer.data

#     return Response(song_list_data)


# CBV 버전의 DRF API
song_list = ListAPIView.as_view(
    # 데이터 조회
    queryset = Song.objects.all().annotate(title_length=Length("title")),
    # 데이터 조정
    serializer_class = SongSerializer,
)




class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# ViewSET의 .as_view() 메서드는 일반적인 CBV의 as_view()와 인자가 다릅니다
#   최소 5개의 View함수를 만들 수 있습니다.

todo_list_or_new = TodoViewSet.as_view({
    # CBV에는 get, post 메서드가 있고
    # get 요청에는 get 메서드를 호출해서 요청을 처리합니다
    "get": "list",
    "post": "create",
})

todo_detail_or_edit_or_delete = TodoViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})


todo_list = ListAPIView.as_view(
    queryset = Todo.objects.all(),
    serializer_class = TodoSerializer,
)

# RestrieveAPIView
# form 처리에서는 get 요청과 post 요청을 지원했습니다
# API에서는 생성에 대해서는 POST요청만을 받습니다
#   UI 부분은 API에서 신경쓰지 않아요 단지 생성 요청만을 받을뿐

todo_new = CreateAPIView.as_view(
    queryset = Todo.objects.all(),
    serializer_class = TodoSerializer, #Form과 유사한 역할로서 유효성검사, 저장 지원
)

# @api_view(["GET", "POST"])
# def todo_list_or_new(request):
#     if request.method == "GET":
#         return todo_list(request)
#     else:
#         return todo_new(request)



todo_detail = RetrieveAPIView.as_view(
    queryset = Todo.objects.all(),
    serializer_class = TodoSerializer,
)

todo_edit = UpdateAPIView.as_view(
    queryset = Todo.objects.all(),
    serializer_class = TodoSerializer, #Form과 유사한 역할로서 유효성검사, 저장 지원
)

todo_delete = DestroyAPIView.as_view(
    queryset = Todo.objects.all(),
    # serializer_class = TodoSerializer,
)



    # JSON 문자열로 변환 (Serialize)해서, 해당 문자열을 반환
    # song_list_data = [
    #     {
    #         "uid": song.uid,
    #         "rank": song.rank,
    #         "title": song.title,
    #         "artist": song.artist,
    #     }
    #     for song in qs
    # ]
    # song_list_data = serializer.data # 자동 변환이 이루어짐

    # json_string = json.dumps(song_list_data, ensure_ascii=False)
    # return HttpResponse(json_string, content_type="application/json")


urlpatterns= [
    path("songs/", song_list),
    path("todos/", todo_list_or_new),
    path("todos/<int:pk>/", todo_detail_or_edit_or_delete)
]


