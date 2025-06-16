# 1. 라이브러리 설치 : openai
# 2. api key 미지정

from openai import OpenAI
client = OpenAI(api_key="up_hZdd3bVmhON7bs2aAcbd6m7n3MoBp",
                base_url="https://api.upstage.ai/v1",
                )

messages: list[dict] = [
    {
        "role": "user", # system, user, assistant, fuction, ...
        "content": "배고파! 서울역 주변 맛집 알려줘! 블로그 후기나 웹에서 후기를 찾을 수 있는 곳으로만!",
    }
]

# stream 여부에 따라 반환값이 달라요
completion = client.chat.completions.create(
    model="solar-pro2-preview", #7/15까지 무료
    messages=messages
)

# stream이 아닐 때 받는 것
print(completion.choices[0].message.content)
