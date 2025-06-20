# 이 파일은 장고 프로젝트 외적인 파일입니다.
# 장고 밖에서 장고의 리소스를 활용해보고
# LLM을 통해서 블로그 포스팅을 생성해보겠습니다.

# 모든 장고를 활용하려는 파이썬 코드는 무조건 DJANGO SETTINGS MODULE 환경 변수 지정이 필요하다
# 현재의 파이썬 코드를 통해 사용할 settings의 경로를 알려줘야만 합니다.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from pyhub.llm import OpenAILLM, UpstageLLM
from pydantic import BaseModel
from django.conf import settings
from blog.models import Post

class BlogPost(BaseModel):
    title: str
    content: str

llm = OpenAILLM(
    api_key=settings.OPENAI_API_KEY,
    # model="gpt-4o",  # dall-e-3
    system_prompt="""
        너는 여행 블로거야. 유저가 제시하는 내용에 맞춰,
        블로그의 제목과 내용을 1000자 이상 작성해줘.
    """,
    max_tokens=8000,
)

keyword_list = [
    "수원 맛집",
    "광주 맛집",
    "울산 맛집"
]

for keyword in keyword_list:
    reply = llm.ask(
        keyword, # 질문내용이 들어가야함
        schema=BlogPost,
        # 원래 pyhub-llm 내부에서 자동으로 대화내역을 관리합니다
        # 현재의 요청은 이게 필요 없으므로 이 옵션 지정 필요
        use_history=False
        )
    print(reply)
    blog_post: BlogPost = reply.structured_data
    blog_post.title # str
    blog_post.content # str

    post = Post()
    post.title = blog_post.title
    post.content = blog_post.content
    post.save()

    print("saved post #", post.id)

# print(reply.text) # > 제목과 내용이 붙어나옵니다
# 제목, 내용 따로 해보자


# from blog.models import Post
# qs = Post.objects.all()
# print("posts :", qs)




