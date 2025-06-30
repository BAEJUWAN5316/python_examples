from django.contrib import admin
from .models import Shop, Review

# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass