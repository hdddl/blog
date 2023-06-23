from django.contrib import admin
from diary.models import Diary
from article.convert import markdown2html


# Register your models here.
class auto_update(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        html = markdown2html(obj.markdown_text, template=True, standalone=True)
        obj.html_text = html
        obj.save()
        super().save_model(request, obj, form, change)


class DiaryAdmin(auto_update):
    list_display = ('pubData',)
    search_fields = ('pubData',)
    exclude = ('html_text', )


admin.site.register(Diary, DiaryAdmin)
