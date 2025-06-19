from django import forms
from chat.models import PuzzleRoom

# forms.Form : 입력 HTML Form과의 인터페이스
# > 입력 폼 html 생성
# > 유저가 입력한 값에 대해서 유효성 검사
# > 유효성 검사에 통과한 값들을 정리도 해줌
# 이건 여기에 직접 model을 써줘야함!

# models.Model : 데이터베이스와의 인터페이스

# forms.ModelForm
# 즉 이건 models.py랑 연동시켜주는 것!

# 상속문법 사용
class PuzzleRoomForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        # 지정 모델의 모든 필드 내역을 빌려와서 폼 필드를 자동으로 구성해줘
        # 유저는 이미지와 level 필드 모두 변경가능!
        fields = "__all__"

class PuzzleRoomEditForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        # 지정 모델의 지정 필드 내역을 빌려와서 폼 필드를 자동으로 구성해줘
        # 유저는 level 필드만 변경가능!
        # 즉 지정 필드만 변경할 수 있게 설정!
        fields = ["level"]