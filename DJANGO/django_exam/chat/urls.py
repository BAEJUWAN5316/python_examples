from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("puzzle/", views.puzzleroom_list),
    path("puzzle/<int:id>/", views.puzzleroom_play),
    path("puzzle/new", views.puzzleroom_new),
]