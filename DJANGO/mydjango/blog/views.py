from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from blog.forms import CommentForm
from blog.models import Comment

# 최소한의 동작을 하는 post 모델에 대한 view(class base view 활용)
#  -. as_view 호출을 통해, view 함수를 만들어주는 클래스

# 이건 무조건 써줘야 하는 관례가 있다!

# 목록 조회 : 모델 클래스

post_list = ListView.as_view(
    model=Post, #여기까진 필수로 들어가야 구동된다
    # 가급적 추천하는 이름으로 만들어주자!
)
# as_view에는 많은 기능들이 있다!
# 다음주에 배울 예정


# 단건 조회 : 모델 클래스
post_detail = DetailView.as_view(
    model=Post,
)

# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, "blog/post_detail.html", {"post": post})

# 댓글 생성 : 모델 클래스, 폼 클래스
comment_new = CreateView.as_view(
    model=Comment,
    form_class=CommentForm,
    success_url="/blog/",
)


# 수정 : 모델 클래스, 폼 클래스
# 단건 조회 : 모델 클래스
# 삭제 : 모델 클래스





