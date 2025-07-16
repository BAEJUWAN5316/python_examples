# from django import forms
from rest_framework import serializers
from melon.models import Song, Todo


# serializers.Serializer # forms.Form과 같음
# serializers.ModelSerializer # forms.ModelForm과 같음

# 변환, 요청 처리
class SongSerializer(serializers.ModelSerializer):
    # 모델 필드에는 없는 이름이어야한다! 존재하면 덮어쓰기가 돼버림
    # title_length = serializers.SerializerMethodField()

    # # 파이썬 단에서 song.title을 계산하는 것이 느리지 않다! 충분한 성능.
    # def get_title_length(self, song) -> int:
    #     return len(song.title)

    # 조회 요청에서만 사용되고, 쓰기 요청에서 이 필드는 무시됩니다
    title_length = serializers.IntegerField(read_only=True)

    class Meta:
        model = Song
        # fields = "__all__" #추천드리지 않아요. 의도치 않게 모델 필드가 api로 노출될 수 있습니다
        fields = ["id", "rank", "album", "title", "artist", "title_length"]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["pk", "content", "is_done", "created_at", "updated_at"]