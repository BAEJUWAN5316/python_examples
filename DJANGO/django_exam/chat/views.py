from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from chat.models import PuzzleRoom
from chat.forms import PuzzleRoomForm
# from chat.models import PuzzleRoom

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html")

def abcd(request, num):

    question = "우짜라고"
    if num >= 10:
        num2 = "하하"
    else:
        num2 = "룰라"

    return render(request, "chat/random.html", context={"question": question, "num2": num2})

from chat.models import PuzzleRoom

def puzzleroom_play(request: HttpRequest, id: int) -> HttpResponse:

    room = PuzzleRoom.objects.get(id=id)
    image_url = room.image_file.url
    level = room.level

    return render(
        request,
        template_name="chat/puzzle.html",
        context={"image_url": image_url, "level": level},
    )

def puzzleroom_list(request):
    qs = PuzzleRoom.objects.all()
    return render(
        request,
        template_name="chat/puzzleroom_list.html",
        context={"puzzleroom_list": qs}
    )

def puzzleroom_new(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = PuzzleRoomForm()

    else:
        form = PuzzleRoomForm(data= request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/chat/puzzle/")
        else:
            pass
    
    return render(request, "chat/puzzleroom_form.html", {
        "form": form
    })