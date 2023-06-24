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


@admin.action(description="刷新")
def update_diary(model_admin, request, queryset):
    for obj in queryset:
        obj.html_text = markdown2html(obj.markdown_text, template=True, standalone=True)
        obj.save()


class DiaryAdmin(auto_update):
    list_display = ('pubDate', 'desc', diary_url)
    search_fields = ('pubData',)
    exclude = ('html_text',)
    actions = [update_diary]


admin.site.register(Diary, DiaryAdmin)
