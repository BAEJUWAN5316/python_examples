from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.urls import path
from blog.models import Post
from blog.api.serializers import PostSerializer, PostListSerializer


post_list = ListAPIView.as_view(
    queryset = Post.objects.published(),
    serializer_class = PostListSerializer,
)

post_detail = RetrieveAPIView.as_view(
    queryset = Post.objects.published(),
    serializer_class = PostSerializer,
)

urlpatterns = [
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),
]