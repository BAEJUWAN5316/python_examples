# 1. 라이브러리 설치 : openai
# 2. api key 미지정

from openai import OpenAI
# client = OpenAI(api_key=)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "i'm hungry!",
        }
    ]
)

print(completion.choices[0].message.content)