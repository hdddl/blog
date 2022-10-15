from urllib.parse import quote
from django.shortcuts import render
from reading.models import Books, Notes


# Create your views here.

def book_index(request):
    objs = Books.objects.all()
    books = []
    for i in objs:
        books.append(
            {
                "title": i.title,
                "author": i.author,
                "nums": i.note_nums,
                "url": "/reading/notes?title=" + quote(i.title)
            }
        )
    return render(request, "reading_index.html", context={"books": books})


def book_notes(request):
    title = request.GET.get("title")
    objs = Notes.objects.filter(book_name__title=title)
    notes = []
    for i in objs:
        notes.append({
            "content": i.content,
            "date": i.note_time,
            "location": i.note_location
        })
    return render(request, "reading_notes.html", context={"notes": notes})
