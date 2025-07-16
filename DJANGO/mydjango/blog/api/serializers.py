from rest_framework import serializers
from blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "status",
            "created_at",
            "updated_at",
        ]


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            # "content", > content 필드는 노출하지 않습니다.
            "status",
            "created_at",
            "updated_at",
        ]