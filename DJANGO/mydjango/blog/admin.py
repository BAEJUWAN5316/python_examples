# blog/admin.py

from django.contrib import admin
from .models import Post

# 모델을 admin에 등록하는 첫번째 방법
#  - 디폴드 admin 옵션으로 등록할 때
#  디폴트 admin: 완전 기본상태의 어드민
# admin.site.register(Post)


#  2번방법
# 약간 커스터마이징 된 admin 만들기
# class PostAdmin(admin.ModelAdmin):
    # pass
# admin사이트에 등록할 건데 PostAdmin의 내용에 따라 구현하라! 라는 뜻
# admin.site.register(Post, PostAdmin)


# 3번방법
@admin.register(Post) # 데코레이터 문법
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
    search_fields = ["title"]
    list_filter = ["status"]

