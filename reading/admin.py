from django.contrib import admin
from reading.models import Books, Notes, KindNotes
from reading.kindle import render


class auto_update(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        data = render(obj.content)      # 渲染获得数据
        for i in data:
            book = Books()
            book.title = i['name']
            book.author = i['author']
            book.save()
            for j in i['marks']:
                note = Notes()
                note.note_time = j['time']
                note.note_location = j['address']
                note.content = j['content']
                note.book_name = book
                note.save()
        super().save_model(request, obj, form, change)


# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')


class NotesAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'content')
    list_filter = ('book_name',)
    search_fields = ('book_name', 'content')


class KindNotesAdmin(auto_update):
    list_display = ("refresh_date",)


admin.site.register(Books, BooksAdmin)
admin.site.register(Notes, NotesAdmin)
admin.site.register(KindNotes, KindNotesAdmin)
