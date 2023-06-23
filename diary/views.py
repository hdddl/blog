from django.shortcuts import render
from diary.models import Diary
from django.http import HttpResponse
from blog.env import HOST


# Create your views here.

def diary_index(request):
    if not request.user.is_authenticated:
        return HttpResponse("404 Not found")
    diaries = []
    for i in Diary.objects.all():
        diaries.append({
            "date": i.pubData,
            "url": HOST + "/diary/diary?date=" + str(i.pubData)
        })
    return render(request, "diary_context.html", context={"diaries": diaries})


def diary_context(request):
    if not request.user.is_authenticated:
        return HttpResponse("404 Not found")
    diary_obj = Diary.objects.filter(pubData=request.GET.get("date"))[0]
    return HttpResponse(diary_obj.html_text)