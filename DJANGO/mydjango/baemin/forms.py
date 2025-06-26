# 리뷰에서는 리뷰 내용과 평점(1~5)사이 넣기

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "rating"]