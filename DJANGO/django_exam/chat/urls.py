from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexxx),
    path("dragon/<int:num>/", views.abcd),
]