from django.db import models


class Post(models.Model):
    # choices는 2개의 값으로 구성된 tuple의 리스트
    STATUS_CHOICES = [
        # 1번은 db에 저장될 값, 2번은 유저에게 보여질 값
        ("draft", "임시"),
        ("published", "공개"),
        ("private", "비공개"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(
        max_length=10, 
        # 모든 모델 필드에서 choices인사를 지원해줍니다
        # 유저로부터의 선택지를 제공하고, 이외의 값에 대해 제한하는 것
        # 악의적인 목적으로 유저가 Form을 변조해서 다른 값을 보내더라도
        # 유효성 검사시에 다 걸러집니다.
        choices=STATUS_CHOICES, 
        default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

# 모델에 기본 키를 지정해서 기본키를 변경하는 방법이 있다.
# 이를 지정하지 않으면 id필드가 자동 생성됩니다
class Comment(models.Model): #models의 모든 클래스는 상속을 받아야 한다!
    # 댓글 길이 제한을두지 않으려면 아래처럼
    # content = models.TextField()

    post = models.ForeignKey( #Post의 기본 키를 가리키는 필드
        Post,
        # on_delete는 포스팅(게시글)이 삭제 되었을 때 댓글은 어떤 처리를 할까?라는 뜻
        on_delete=models.CASCADE #CASCADE는 관련댓글 자동 삭제 기능
        # 이 외에도 Post 삭제 막기, 등등 기능이 있다
    ) 
    content = models.CharField( #field의 속성을 선택할 수 있음 글자수 제한 등
        max_length=1000,
    )
