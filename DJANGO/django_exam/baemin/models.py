from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField()

class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(
        choices=[
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