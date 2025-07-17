from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.urls import path
from blog.api.serializers import PostSerializer, PostListSerializer


post_list = ListAPIView.as_view(
    # only:지정 필드만 조회 <=> defer: 지정 필드만 빼기
    # queryset = Post.objects.published().defer("content").select_related("author"), # select_related가 있어야 데이터베이스에 n+1현상이 일어나지 않는다!
    queryset = PostListSerializer.get_optimized_queryset(),
    serializer_class = PostListSerializer,
)

post_detail = RetrieveAPIView.as_view(
    queryset = PostSerializer.get_optimized_queryset(),
    serializer_class = PostSerializer,
)

urlpatterns = [
    path("posts/", post_list),
    path("posts/<int:pk>/", post_detail),
]