# 1. 라이브러리 설치 : openai
# 2. api key 미지정

from openai import OpenAI
client = OpenAI(api_key="up_hZdd3bVmhON7bs2aAcbd6m7n3MoBp",
                base_url="https://api.upstage.ai/v1",
                )

completion = client.chat.completions.create(
    model="solar-pro2-preview", #7/15까지 무료
    messages=[
        {
            "role": "user",
            "content": "hello",
        }
    ]
)

print(completion.choices[0].message.content)