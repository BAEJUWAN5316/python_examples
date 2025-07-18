from django.urls import path, include
from. import views

# 장고의 urls.py에게 장고가 요구하는 것은 단 하나!
# urlpatterns이름의 리스트 > 이름의 오타가 있으면 안 된다!

app_name = "blog"
# 앱 이름과 동일하게 지정해주면 됩니다

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("new/", views.post_new, name="post_new"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<int:post_pk>/comments/new/", views.comment_new, name="comment_new"),
    path("<int:post_pk>/comments/<int:pk>/edit/", views.comment_edit, name="comment_edit"),
    path("api/v1/", include("blog.api.v1"))
]