from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    def clean_username(self): #clean_user는 장고에서 약속된 이름!
        # 이 매서드는 유효성 검사시에 자동으로 호출됩니다
        username = self.cleaned_data.get("username")
        if username:
            if username in ["trump"]:
                raise ValidationError("허용되지 않은 유저명입니다.")
        return username