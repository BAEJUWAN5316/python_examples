from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Review
from .forms import ReviewForm
from django.contrib import messages

def shop_list(request):
    qs = Shop.objects.all()

    return render(
        request, 
        "baemin/shop_list.html", 
        context={"shop_list":qs
        })

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    image_url = shop.photo.url
    review_qs = Review.objects.all()
    review_qs = review_qs.filter(shop=shop)

    return render(
        request,
        "baemin/shop_detail.html",
        context={"shop":shop, "image_url":image_url, "review_list":review_qs}
    )


def review_new(request, shop_pk):
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "GET":
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_comment: Review = form.save(commit=False)
            unsaved_comment.shop = Shop.objects.get(id=shop_pk)
            unsaved_comment.save()

            messages.success(request, "리뷰작성완료")

            shop_url = f"/baemin/{shop_pk}/"
            return redirect(shop_url)
    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form":form}
    )

