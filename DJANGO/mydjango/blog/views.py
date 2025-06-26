from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from blog.forms import CommentForm
from blog.models import Comment
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

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
# comment_new = CreateView.as_view(
#     model=Comment,
#     form_class=CommentForm,
#     success_url="/blog/",
# )

# View 구현에서 반복을 줄일 수 있도록 줄일 수 있도록 도와주는 장고의 기능 : Class Based View
# Form 요청을 위해 하나의 주소에서 get요청과 post 요청을 같이 받습니다 > django스타일
# django 라면 : 주소에 기반헤서 호출된 View 매핑 > 하나의 주소 > 하나의 view > 하나의 함수
# java spring 이라면 : blog/comments/form/ 에서 get 요청 blog/commetns/submit 에서 post 요청
#       다른 두 개의 url로 기능을 나눔
#           >> 2개의 함수가 필요해진다! >> 반복횟수 올라감
def comment_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    # HTML <form>요청에서는 method는 단 2가지 > GET or POST
    # <form method="post">라고 썻다고 해도 장고서버에서는 항상 대문자
    if request.method == "GET":
        form = CommentForm()
    else: # get이 아니라면? > 무조건 post > 즉 포스트 일 때 일어날 기능
        # 제출 받은 값들을 장고 Form에게 제출해야합니다
        # django view에서 요청받은 데이터 참조하는 법
        #   1. request.GET
        #   2. request.POST : 파일을 제외한 POST데이터
        #   3. request.files : 파일로만 구성된 POST데이터
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid(): # > 입력받은 모든 값에 대해 유효성 검사를 싹 다 해준다
            # django Form은 아래의 사전을 생성해주는 것까지만
            # > 저장에 db저장까지는 해주지 않음
            # form.cleaned_data # dict타입으로 유효성 검사를 통과한 값들이 담김
            # 그럼 이제 db에 저장을 시켜줘야함
            # django ModelForm을 이용해서 저장해주자!
            unsaved_comment: Comment = form.save(commit=False) # 이건 바로 db에 저장 시켜주는 것, modelform의 save
            # saved_comment.content > 자동으로 지정되니 신경 안 써줘도 된다
            # commit=False를 지정하면 from.save 내부에서 모델.save()를 호출하지 않는다
            #  >> 모델 인스턴스만 생성하고 반환만 합니다
            #  >> 아직 모델.save메서드를 호출하지 않은 상황

            # 유저로 부터 Post를 지정받지 않는다! 라고 해서 
            # Post필드 값을 지정하지 않아도 되는 것은 아닙니다
            # 프로그램 코드를 통해 자동 지정되도록 해야합니다
            unsaved_comment.post = Post.objects.get(id=post_pk)
            # 이건 게시물의 id지만 유사한 예로는 유저의 ip, 유저의 웹브라우저 종류 등
            unsaved_comment.save() # > model의 save
            # 대개의 서비스 기획: 생성폼에서 생성 성공하면 다른 페이지로 이동한다!

            # Model의 save()
            #  > 데이터 베이스로 지정 필드 구성으로 저장을 시도

            # ModelForm의 save
            #  > cleaned_data dict값을 기반으로
            #   Model 인스턴스를 만들어서 모델의 save를 호출합니다

            post_url = f"/blog/{post_pk}/"
            return redirect(post_url) #> 브라우저에게 이동하라는 지시! 이 주소로 가라!는게 redircet


    return render(request, "blog/comment_form.html", {
        "form":form,
    })



# 수정 : 모델 클래스, 폼 클래스
# 단건 조회 : 모델 클래스
# 삭제 : 모델 클래스





