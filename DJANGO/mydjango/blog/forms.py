from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 전체 필드를 지정할 때는 리스트 안 써도 된다 그냥 아래 처럼 쓰면 된다
        fields= "__all__"