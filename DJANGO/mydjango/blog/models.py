from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User
# 장고에서 기본으로 지원하는 User모델
# 추가기능을 넣고싶다면 수정도 가능하다
# 단, 최초 migrate 하기 전에 수정하자.
# 이후에도 할 수는 있지만 조금 복잡해서 학생은 db에러가 뜰 수 있다!
# 매 요청을 처리할 때마다 db에서 관련 user를 조회합니다. request.user속성
# 하지만 유저 관련 필드들은 별도의 모델로 관리하는 것을 추천합니다
# auth라는 앱의 User라는 모델을 쓴다는 뜻


class PostQuerySet(models.QuerySet):
    def draft(self):
        return self.filter(status=Post.Status.DRAFT)
    
    def published(self):
        return self.filter(status=Post.Status.PUBLISHED)
    
    def private(self):
        return self.filter(status=Post.Status.PRIVATE)

class Post(models.Model):
    # choices는 2개의 값으로 구성된 tuple의 리스트
    # STATUS_CHOICES = [
    #     # 1번은 db에 저장될 값, 2번은 유저에게 보여질 값
    #     ("draft", "임시"),
    #     ("published", "공개"),
    #     ("private", "비공개"),
    # ]
    class Status(models.TextChoices):
        DRAFT = "draft", "임시"
        PUBLISHED = "published", "공개"
        PRIVATE = "private", "비공개"

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(
        max_length=10, 
        # 모든 모델 필드에서 choices인사를 지원해줍니다
        # 유저로부터의 선택지를 제공하고, 이외의 값에 대해 제한하는 것
        # 악의적인 목적으로 유저가 Form을 변조해서 다른 값을 보내더라도
        # 유효성 검사시에 다 걸러집니다.
        choices=Status.choices, 
        default=Status.DRAFT,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostQuerySet.as_manager()


    def __str__(self):
        return self.title
    
    def get_absolute_url(self) -> str:
        # Post 모델에 대한 detail 주소 문자열(/로 시작하는)을 반환하는 함수
        return reverse("blog:post_detail", kwargs={"pk":self.pk})
    

# 모델에 기본 키를 지정해서 기본키를 변경하는 방법이 있다.
# 이를 지정하지 않으면 id필드가 자동 생성됩니다

# sql을 직접 작성하지 않아도 django model로 작성을 하면
# database에 대한 조회, 생성, 수정, 삭제 등을 요청할 수 있게 된다
#  >모델이란 것은 database에 접근해서 무언가를 조작할 수 있게 해주는 것!
# - SQL은 지금 잘 몰라도 하면서 이해도를 높이다 보면 효율적인 애플리케이션 서비스를 할 수 있다
#   1) 서비스 새발 비용과 유지 보수 비용을 저렴하게 가능! > 개발된 코드를 내가/우리가 감당가능한가?
#   2) 서버 운영 비용을 낮출 수 있고, 유저에게 보다 빠른 서비스 응답을 줄 수 있습니다
class Comment(models.Model): #models의 모든 클래스는 상속을 받아야 한다!
    # 댓글 길이 제한을두지 않으려면 아래처럼
    # content = models.TextField()

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, blank=False, null=False)
    # blank=False, null=False 는 기본값.
    # balnk는 form 입장에서 빈 입력필드를 허용할 지 여부
    # null은 db입장에서 빈 값을 넣게 허용할지 여부
    # 두 필드 모두 거짓이면 이 필드는 필수 필드가 된다!

    post = models.ForeignKey( #Post의 기본 키를 가리키는 필드
        Post,
        # on_delete는 포스팅(게시글)이 삭제 되었을 때 댓글은 어떤 처리를 할까?라는 뜻
        on_delete=models.CASCADE #CASCADE는 관련댓글 자동 삭제 기능
        # 이 외에도 Post 삭제 막기, 등등 기능이 있다
    ) 
    content = models.CharField( #field의 속성을 선택할 수 있음 글자수 제한 등
        max_length=1000,
    )
    tags = models.CharField(max_length=100, default="")
