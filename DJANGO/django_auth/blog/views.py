from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

#게시글 작성기능 구현
# /blog/write

def post_new(request):
    # 로그인 여부를 판단
    # 미 로그인 상황에서는 로그인 주소로 이동시키기
    if not request.user.is_authenticated:
        return redirect("/login")
    
    return render(request, "blog/post_form.html")

# 게시글 목록 기능 구현
# /blog/
def post_list(request):
    return render(request, "blog/post_list.html")

# 게시글 상세보기 기능 구현
# /blog/<int:id>
def post_detail(request, id: int):
    return render(request, "blog/post_detail.html")

#게시글 검색 기능
# /blog/search/<str:tag>
def post_search(request, tag: str):
    # qs = Post.objects.all()
    # qs = qs.filter()
    return render(request, "blog/post_search.html")

# 게시글 수정 기능 구현
# /blog/edit/<int:id>
def post_edit(request, id: int):
    post = get_object_or_404(post, id=id)
    # 글 작성자 정보가 post.author라는 User모델 외래키 필드가 있다면!


    if not request.user.is_authenticated:
        messages.info(request, "글을 수정하려면 로그인이 필요합니다.")
        return redirect("/login")
    # 본인 글이 아니라면,
    # 1> 로그인 페이지로 보낼까
    # 2> 에러 템플릿 응답을 할까
    if request.user != post.author:
        messages.info(request, "본인 글만 수정할 수 있습니다.")
        return redirect("/login")
    return render(request, "blog/post_form.html")

# 게시글 삭제 기능 구현
# /blog/delete/<int:id>
def post_delete(request, id: int):
    return render(request, "blog/post_confir_delete.html")