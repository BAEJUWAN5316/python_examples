from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


# 1측
class Shop(models.Model):
    name = models.CharField(max_length=100) # 길이제한 있는 것
    description = models.TextField() # 길이제한 없는 것
    # photo = models.FileField() #모든 포맷 파일 가능
    photo = models.ImageField() # 이미지 파일만 가능
    
    class Meta:
        ordering = ["-id"] #정렬 지정은 항상 하자!

# 장고의 유효성 검사 함수 인자는 항상 1개만 받고요
# 그 값이 정해진 규칙에서 벗어날 때 ValidatrError을 발생
# 정해진 규칙에 부합이 될 때에는 Nothing to do. 아무것도 하지않고 함수 종료, 반환값 필요x
# def validator_min_1(value):
#     # 인자의 값이 1이상 이기를 기대합니다
#     if value < 1:
#         raise ValidationError("값이 1 이상이어야 합니다")
#     #  >>>> 이런 식으로 조건 검사를 해줄 수 있는 함수를 여러개 만들 수 있다!

# def validator_min_3(value):
#     # 인자의 값이 3이상 이기를 기대합니다
#     if value < 3:
#         raise ValidationError("값이 3 이상이어야 합니다")
    # 하지만 이렇게 매번 만드는 건 비효율적이다!!
# 그러니까 위 함수를 만들어주는 함수를 만들어보자!

def make_validator_min(min_value):
    def validator_func(value):
        if value < min_value:
            raise ValidationError(f"값이 {min_value}이상이어야 합니다")
        
    return validator_func
# 중복함수 연습해보자

validator_min_3 = make_validator_min(3)

#  N측에 1에 대한 외래키 필드를 추가
class Review(models.Model):
    # user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    # rating = models.IntegerField() # 음수/양수 다 담을 수 있음
    # 근데 음수가 담기지 않을 거라면? 양수만 담으면 된다!
    # rating = models.PositiveIntegerField() # > 양수만 담으니까 담을 수 있는 숫자가 두배!
    rating = models.PositiveSmallIntegerField(
        # validator: 입력된 값에 대해 유효성 검사를 해주는 다수의 함수
        # validators=[
        #     MinValueValidator(1), 
        #     # make_validator_min(1), # 함수가 함수를 생성한 버전
        #     MaxValueValidator(5) # 클래스를 함수처럼 사용한 버전
        #                             # 하지만 장고에서 기본으로 지원하는 validator를 사용하세요
        # ],
        choices=[ #모든 모델 필드에서 제공, 드롭다운으로 선택 가능하게 해줌
            (1, "1점"),
            (2, "2점"),
            (3, "3점"),
            (4, "4점"),
            (5, "5점"),
        ],
        help_text="1점~5점 사이 점수를 주세요"
    ) #

    # Review 쿼리셋에 대한 디폴트 정렬
    #  - Review 쿼리셋에서 order_by를 지정하지 않으면, 자동으로 적용됩니다.
    class Meta:
        ordering = ["-id"]
    # 1bit > 0 과 1만을 표현하는 컴퓨터의 최소단위 > 값을 2가지 표현가능
    # 2bit > 2**2 = 총 4가지 가능
    # 3bit > 2**3 = 8가지 가능.. 등등등
    # 1byte = 8bit
    # 일반적인 숫자 변수는 4바이트(32bit)로 숫자를 표현 8바이트(64bit)도 가능
