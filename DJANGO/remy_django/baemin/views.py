from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Review
from .forms import ReviewForm


def shop_list(request):
    qs = Shop.objects.all()
    return render(
        request,
        "baemin/shop_list.html",
        context={"shop_list":qs}
    )


def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    image_url = shop.photo.url
    return render(
        request,
        "baemin/shop_detail.html",
        context={"shop":shop, "image_url":image_url}
    )


def review_new(request, shop_pk):

    if request.method == "GET":
        form = ReviewForm()
    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
    return render(
        request,
        "baemin/review_form.html",
        context={"form":form}
    )