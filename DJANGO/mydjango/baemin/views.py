from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Shop, Review
from .forms import ReviewForm
from django.http import Http404
from django.http import HttpRequest, HttpResponse

class ShopListView(ListView):
    model = Shop
    paginate_by = 3
    # 아래 설정이 디폴트 설정
    # 아무것도 쓰지 않으면 아래와 같아진다!
    # template_name = "baemin/shop_list.html"
    # 요청에 따라 사용하는 탬플릿을 변경해봅시다

    def get_template_names(self):
        if "naked" in self.request.GET:
            return "baemin/_shop_list.html"
        # 아래의 코드는 원래 매서드의 기본 동작을 수행
        return super().get_template_names()


# 클래스를 통해서 새로운 view 함수 생성하기!
# 아래는 코드라기 보다 설정에 가까운 내용!
shop_list = ShopListView.as_view()

# 최신의 가게 목록 페이지를 보여줄 거예요/
# - 최신이ㅡ 데이터는 DB안에 있죠 그러니 매번 DB 조회를 할 겁니다
# def shop_list(request):
#     # 데이터베이스에서 baemin_shop테이블의 모든 레코드를
#     # 조회할 준비(아직 데이터를 가져오진 않았습니다)
#     qs = Shop.objects.all() # QuerySet타입!

#     # page = 3
#     page = int(request.GET.get("page", 1)) #쿼리스트링 값은 기본적을 str타입!
#     paginate_by = 5 # 몇 개의 게시물씩 끊어서 페이징 하겠는지 설정!

#     # qs = qs[0:5] # 문자열의 슬라이싱과 동일, 1페이지: 처음 5개
#     # qs = qs[5:10] # 2페이지
#     # qs = qs[10:15] # 3페이지
#     # 이런 식이니까 아래처럼 하면 게시물에 맞춰서 계속 나뉘어 진다
    
#     start_index = (page - 1) * paginate_by
#     end_index = page * paginate_by
#     qs = qs[start_index:end_index]

#     return render(
#         request, 
#         template_name="baemin/shop_list.html",
#         context={
#             "shop_list":qs,
#         })

# TODO: baemin/shop_list.html 템플릿을 만들어보기. 하얀 배경도 OK. chatgpt 등을 통한 코드 생성도 OK

def shop_detail(request, pk):
    # shop = Shop.objects.get(pk=pk) .get이 .get_object_or_404와 겹친다! 뒤에껀 자동으로 get에서 없을 때 404 보여주는 거!
    
    shop = get_object_or_404(Shop, pk=pk)
    image_url = shop.photo.url

    # 정렬(sort) : 정렬 기준으로 2개 이상 둘 수도 있습니다
    # 각 정렬은 오름차순, 내림차순을 지정할 수 있어요
    # 그런데, 가급적 정렬 기준 컬럼은 1개마 지정하길 권장
    #  - 데이터베이스가 적으면 (몇 천개) 아무 상관 없습니다
    #  - 데이터베이스가 정렬을 요청 받으면 정렬을 모두 한 후에 응답을 하죠
    #  - 정렬 기준이 여러개면 그만큼 응답시간이 오래 걸립니다
    #  - 대개의 경우 정렬은 1개 기준이면 충분!

    # 전체 리뷰(모든 Shop) 데이터를 가져올 준비
    # 하지만 우리가 필요한건 현재 가게에 대한 리뷰!
    review_qs = Review.objects.all()
    # 특정 shop의 리뷰 데이터를 가져올 준비 완료
    review_qs = review_qs.filter(shop=shop)

    # 정렬을 지정하지 않아도 출력은 된다! > 지정하지 않으면 오름차순?
    #  > 정렬을 지정하지 않으면 저장된 순서대로 조회될 뿐!
    #  > 조회할 때마다 다른 순서로 조회가 될 수 도 있습니다

    # review_qs = review_qs.order_by("-id") # id 필드 역순(내림차순)
    # review_qs = review_qs.order_by("id") # id 필드순(오름차순)

    return render(
        request,
        template_name="baemin/shop_detail.html",
        context={"shop": shop, "image_url": image_url, "review_list": review_qs}
    )


# 반드시 로그인 상태에서만 리뷰 폼이 보여져야합니다
# @login_required > 이거를 데코레이터로 적용하면 로그인 상황이 아니면 자동으로 로그인 페이지로 보냅니다
def review_new(request, shop_pk):
    # shop = Shop.objects.get(pk=shop_pk) 

    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "GET":
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid(): # > 입력받은 모든 값에 대해 유효성 검사를 싹 다 해준다
            unsaved_comment: Review = form.save(commit=
                                                False) 
            unsaved_comment.shop = Shop.objects.get(id=shop_pk)
            # unsaved_comment.user = request.user
            unsaved_comment.save()

            messages.success(request, "고객님의 리뷰에 감사드립니다! ;")
            # 위 메세지는 요청을 한 유저에게만 보여질 거예요.

            shop_url = f"/baemin/{shop_pk}/"
            return redirect(shop_url) 

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form":form}
    )


def review_edit(request, shop_pk, pk):
    # 모델클래스.object > Model Manager라고 부른다
    #  ,all
    #  .get
    #  .filter
    #  .exclude
    #  .order_by 등

    # 지정 조건의 레코드가 DB에 없을 때 Reveiw.DoesNotExist 예외가 발생합니다
    # try:
    #     review = Review.objects.get(pk=pk) # 지정 조건의 레코드가 데이터베이스에 1개 있어야 한다!
    # except Review.DoesNotExist:
    #     raise Http404
    
    # 위처럼 해도 되지만 아래처럼 아주 쉽게 해줄 수도 있다!
    review = get_object_or_404(Review, pk=pk)

    if request.method == "GET":
        form = ReviewForm(instance=review)
    else:
        form = ReviewForm(instance=review, data=request.POST, files=request.FILES)
        if form.is_valid(): # > 입력받은 모든 값에 대해 유효성 검사를 싹 다 해준다
            # 리뷰 수정 시에는 ReviewForm 클래스 안에서 정의된 필드에 대해서만
            # 저장되어도 된다
            # 즉 새로 뭔가 만들 필요 없다는 것!
            form.save() 
            messages.success(request, "고객님의 리뷰가 수정되었습니다! ;")
            # 위 메세지는 요청을 한 유저에게만 보여질 거예요.

            shop_url = f"/baemin/{shop_pk}/"
            return redirect(shop_url) 

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form":form}
    )

# 장고 스타일의 삭제 방식
#  1) GET 요청: 삭제를 요청했을 때 > 확인 과정을 거칩니다(정말 삭제할 것이냐?)
#  2) POST 요청: 삭제 확인 > 삭제 진행
def review_delete(request: HttpRequest, shop_pk: int, pk: int) -> HttpResponse:
    if request.method == "GET":
        return render(request, "baemin/review_confirm_delete.html")
    
    review = get_object_or_404(Review, pk=pk)
    review.delete() # 데이터베이스에서 호출 즉시 삭제됩니다.
    
    messages.success(request, "지정 리뷰를 삭제했습니다.")

    shop_url = f"/baemin/{shop_pk}"
    return redirect(shop_url)