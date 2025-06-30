from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


# 1측
class Shop(models.Model):
    name = models.CharField(max_length=100) # 길이제한 있는 것
    description = models.TextField() # 길이제한 없는 것
    photo = models.ImageField() # 이미지 파일만 가능
    class Meta:
        ordering = ["-id"] #정렬 지정은 항상 하자!


class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(
        choices=[ #모든 모델 필드에서 제공, 드롭다운으로 선택 가능하게 해줌
            (1, "1점"),
            (2, "2점"),
            (3, "3점"),
            (4, "4점"),
            (5, "5점"),
        ],
        help_text="1점~5점 사이 점수를 주세요"
    ) 
    class Meta:
        ordering = ["-id"]
