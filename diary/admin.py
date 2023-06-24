from django.contrib import admin
from django.utils.safestring import mark_safe
from diary.models import Diary
from article.convert import markdown2html


# Register your models here.
class auto_update(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        html = markdown2html(obj.markdown_text, template=True, standalone=True)
        obj.html_text = html
        obj.save()
        super().save_model(request, obj, form, change)


def diary_url(obj):
    url = "/diary/diary?date=" + str(obj.pubDate)
    return mark_safe('<a href="%s" target="_blank">redirect</a>' % url)


class DiaryAdmin(auto_update):
    list_display = ('pubDate', 'desc', diary_url)
    search_fields = ('pubData',)
    exclude = ('html_text',)


admin.site.register(Diary, DiaryAdmin)
