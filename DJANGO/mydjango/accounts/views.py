from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
#장고 기본 기능!

# Create your views here.

from django.contrib.auth import login as auth_login
# username/password 유효성 검사 후에, auth_login(request) 호출해서 세션 인증토록 구현마시고
# LoginView를 적극 활용해주세요


login = LoginView.as_view(
    template_name="accounts/login_form.html",
    success_url_allowed_hosts=["localhost:3000", "localhost:5173"]
)

logout = LogoutView.as_view()

@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def signup(request):
    if request.method == "GET":
        form = SignupForm()
    else:
        form = SignupForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save() # 회원가입 완료! db에 저장된다
            # 회원가입을 했으니 로그인 페이지로 이동하는게 자연스러움
            return redirect("/accounts/login/")
        
    return render(
        request, 
        "accounts/signup_form.html", 
        context={"form":form})