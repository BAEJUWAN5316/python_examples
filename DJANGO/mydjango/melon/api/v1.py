import json
from django.http import HttpResponse
from django.urls import path
from melon.models import Song
from melon.api.serializers import SongSerializer


def song_list(request):
    qs = Song.objects.all()

    # 데이터 변환의 기능을 제공(시리얼라이저 오리지널 기능)
    #  입력 데이터에 대한 유효성 감사 및 저장(FORM의 기능)
    serializer = SongSerializer(
        instance=qs,
        many=True,
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
    song_list_data = serializer.data # 자동 변환이 이루어짐

    json_string = json.dumps(song_list_data, ensure_ascii=False)
    return HttpResponse(json_string, content_type="application/json")


urlpatterns= [
    path("songs/", song_list)
]


