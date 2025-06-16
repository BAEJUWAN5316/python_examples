# .env 파일을 읽어서, 환경변수로서 로딩!
# django-environ을 이용해서 환경변수를 장고에 불러온다!

from environ import Env # 이게 djangon-environ 라이브러리
from pathlib import Path

BASE_DIR = Path(__file__).parent
ENV_PATH = BASE_DIR / ".env"

env = Env()
env.read_env(ENV_PATH, overwrite=True)

# 이 위까지는 그냥 복붙하는 느낌으로 항상 넣자!
# 지정 경로에 .env가 없어도 예외 발생하지 않는다

# import os
# print(os.environ["HELLO"])
# 환경변수 값을 읽어서 별도의 변수에 할당
#  - 여러 로직에서 매번 환경변수 값에 직접 접근하는 것보다
#    환경변수 접근은 특정 로직에서만 해서
#    그 로직에서 설정 변수를 만들고 다른 로직에서 참조토록 하면
#    훨씬 관리성이 좋습니다.

# 환경변수 값은 항상 문자열(str)

# print(env.str("HELLO"))

# import os
# print(os.environ["UPSTAGE_API_KEY"])

from pyhub.llm import UpstageLLM
# from pyhub.llm import OpenAILLM

# 내부적으로 UPSTAGE_API_KEY 환경변수 값이 있으면,
# 자동으로 활용합니다.
llm = UpstageLLM()
# llm = OpenAILLM(model="gpt-4o-mini") #OPEN_API_LLM 환경변수가 있으면 자동 활용 > 괄호 안에 특별히 어떤 api와 연결 할 지 안 써줘도 된다!

# 아래는 한 번에 받아서 오기때문에 느리다!
# reply = llm.ask("hello")
# print(reply)
# print(reply.usage)

# stream=True 지정하시면, Generator 반환
# for chunk in llm.ask("hello", stream=True):
#     print(chunk.text, end="")
# print()

reply = llm.ask("우울해서 빵을 샀어.", choices=["기쁨", "슬픔", "분노", "불안", "무기력함"])
print(reply.choice)        # "슬픔"
print(reply.choice_index)  # 1
