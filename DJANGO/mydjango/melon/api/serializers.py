# from django import forms
from rest_framework import serializers
from melon.models import Song


# serializers.Serializer # forms.Form과 같음
# serializers.ModelSerializer # forms.ModelForm과 같음

# 변환, 요청 처리
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


