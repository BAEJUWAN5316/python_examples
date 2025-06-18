from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# from chat.models import PuzzleRoom

# Create your views here.
def indexxx(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/indexx.html")

def abcd(request, num):

    question = "우짜라고"
    if num >= 10:
        num2 = "하하"
    else:
        num2 = "룰라"

    return render(request, "chat/random.html", context={"question": question, "num2": num2})