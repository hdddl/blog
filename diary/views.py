from django.shortcuts import render
from diary.models import Diary
from django.http import HttpResponse
from blog.env import HOST


# Create your views here.

def diary_index(request):
    if not request.user.is_authenticated:
        return render(request, "prohibit.html")
    diaries = []
    for i in Diary.objects.all()[::-1]:
        diaries.append({
            "date": i.pubDate,
            "url": HOST + "/diary/diary?date=" + str(i.pubDate),
            "desc": i.desc,
        })
    return render(request, "diary_context.html", context={"diaries": diaries})


def diary_context(request):
    if not request.user.is_authenticated:
        return render(request, "prohibit.html")
    diary_obj = Diary.objects.filter(pubDate=request.GET.get("date"))[0]
    return HttpResponse(diary_obj.html_text)