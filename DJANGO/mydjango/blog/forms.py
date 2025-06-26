from django import forms
from .models import Comment

# forms.Form
#  - get요청 : 지정된 필드 구성으로 유저에게 입력폼 html 생성
#  - post 요청 : 지정된 필드 구성으로 유저에게 제출받은 값들의 유혀성 검사를 수행
#                   -> valid : 유효성 검사에 통과한 값들을 dict타입으로 제공받고 다른 주소로 이동
#                   -> invalid : 유저에게 다시 오류 내역이 포함된 html 생성/응답

# Form : 모델처럼 유저로부터 입력받을 값에 대한 필드 구성을 하나하나 다 해야합니다
# class CommentForm(forms.Form):
#     content = forms.CharField()

# ModelForm이란?
#   - 지정 모델의 지정 필드들의 정보를 읽어와서
#      폼 필드 구성을 자동으로 수행해줍니다
#   - 모델 구성이 바뀌면 알아서 폼 필드도 구성이 변경됩니다
#   > 서버 재시작을 해줘야합니다
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 전체 필드를 지정할 때는 리스트 안 써도 된다 그냥 아래 처럼 쓰면 된다
        # fields= "__all__" > 이건 게시 선택 박스도 있으니 재정의 하자!

        # 유저로 부터 받을 필드만 명시!
        fields = ["content"]
        #  > views.py에서 form.save에 content만 저장을 시도한다
        # all에서 저장되던 id가 누락된 상태!
        # 그러니 views.py를 수정해주자


















