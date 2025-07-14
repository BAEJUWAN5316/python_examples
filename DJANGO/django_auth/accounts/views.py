from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView

def root(request):
    return render(request, "root.html")

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/login")
#     else:
#         form = UserCreationForm()
#     return render(
#         request,
#         "accounts/register.html",
#         {"form":form}
#     )

register = CreateView.as_view(
    form_class=UserCreationForm,
    template_name="accounts/register.html",
    success_url="/login",
)

# 함수 기반 view
# def login(request):
#     pass

# 클래스 기반 view
# 클래스 기반 view에는 항상 as_view()를 넣어줘야한다
login = LoginView.as_view()

logout = LogoutView.as_view()

def profile(request):
    return render(request, "accounts/profile.html")