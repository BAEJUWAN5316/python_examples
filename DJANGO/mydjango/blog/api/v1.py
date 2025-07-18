from django.urls import path
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from blog.api.serializers import PostSerializer, PostListSerializer, PostCreateSerializer
# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from blog.models import Post
from rest_framework.routers import DefaultRouter

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all() #ㄱ정. 가변적으로 줄려면 get_queryser 메서드 구현
    serializer_class = PostSerializer # 고정. 가변적으로 줄려면 get_serializer 메서드를 구현

router = DefaultRouter()
router.register("posts", PostViewSet)
# router.urls



# post_list = ListAPIView.as_view(
#     # only:지정 필드만 조회 <=> defer: 지정 필드만 빼기
#     # queryset = Post.objects.published().defer("content").select_related("author"), # select_related가 있어야 데이터베이스에 n+1현상이 일어나지 않는다!
#     queryset = PostListSerializer.get_optimized_queryset(),
#     serializer_class = PostListSerializer,
# )


# class PostCreateAPIView(CreateAPIView):
#     serializer_class = PostCreateSerializer
#     permission_classes = [IsAuthenticated] # @login_required랑 비슷
    # 이게 있으면 인증되지 않은 상황에서는 요청이 거부됩
    #  = 로그인 하지 않은 상황에서 글쓰기!

    # # 웹페이지에서 로그인 된 상황에서 테스트해봅시다
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    
# post_new = PostCreateAPIView.as_view()

# 아래 모델 시리얼라이저에 지정된 필드 만으로 데이터베이스 저장이 가능할 때에는
# 아래 코드만으로 충분합니다.
# 그런데, 데이터베이스 저장 전에 추가로 할당해야할 필드가 있다면
# 데이터 베이스 저장 전에 할당을 해줘야겠죠
# post_new = CreateAPIView.as_view(
#     serializer_class = PostCreateSerializer,
# )


# post_detail = RetrieveAPIView.as_view(
#     queryset = PostSerializer.get_optimized_queryset(),
#     serializer_class = PostSerializer,
# )


# urlpatterns = [
#     path("", include(router.urls))
# ]

urlpatterns = router.urls

# urlpatterns = [
    # path("posts/", post_list),
#     path("posts/", post_new),
#     path("posts/<int:pk>/", post_detail),
# ]