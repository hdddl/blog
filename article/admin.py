# coding=utf-8
from django.contrib import admin

from .models import Blog, Micro_blog, Categories, Tags, Pages
from .convert import markdown2html


# Register your models here.
class auto_update(admin.ModelAdmin):
    # 重写save_model
    def save_model(self, request, obj, form, change):
        if obj.__class__ == Pages and obj.text_type == "html":
            super().save_model(request, obj, form, change)
            return

        if obj.__class__ == Micro_blog:
            html = markdown2html(obj.markdown_text, template=False, standalone=False)
        else:
            html = markdown2html(obj.markdown_text, template=True, standalone=True)
        obj.html_text = html
        obj.save()
        super().save_model(request, obj, form, change)


class BlogAdmin(auto_update):
    list_display = ('title', 'category', 'visits', 'pubdate')
    exclude = ('visits', 'html_text', 'updated')


class PagesAdmin(auto_update):
    list_display = ('name', 'text_type', 'pubdate')
    list_filter = ('name', 'text_type', 'pubdate')
    exclude = ('updated',)


class MicroBlogAdmin(auto_update):
    list_display = ('pubdate',)
    list_filter = ('pubdate',)
    exclude = ('html_text', 'updated')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Micro_blog, MicroBlogAdmin)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Pages, PagesAdmin)
