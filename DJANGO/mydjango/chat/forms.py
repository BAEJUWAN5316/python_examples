from django import forms
from chat.models import PuzzleRoom

# 상속문법 사용
class PuzzleRoomForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        fields = "__all__"