# coding=utf-8
from django.contrib import admin
from django.utils.safestring import mark_safe

from article.models import Blog, Micro_blog, Categories, Tags, Pages, PageCategories
from article.convert import markdown2html
from blog.env import HOST


# Register your models here.
class auto_update(admin.ModelAdmin):
    # 重写save_model
    def save_model(self, request, obj, form, change):
        if obj.__class__ == Pages and obj.page_type.name == "html":
            super().save_model(request, obj, form, change)
            return
        if obj.__class__ == Micro_blog:     # 如果是微博
            html = markdown2html(obj.markdown_text, template=False, standalone=False)
        else:       # 如果是博客
            html = markdown2html(obj.markdown_text, template=True, standalone=True)
        obj.html_text = html
        obj.save()
        super().save_model(request, obj, form, change)


class BlogAdmin(auto_update):
    list_display = ('title', 'category', 'visits', 'pubdate')
    exclude = ('visits', 'html_text', 'updated')


class PagesAdmin(auto_update):
    # 返回页面所对应的URL
    def page_url(self, obj):
        url = HOST + "/api/pages?name=" + obj.title
        return mark_safe('<a href="%s" target=”_blank”>redirect</a>' % url)

    list_display = ('title', 'page_type', 'pubdate', "page_url")
    list_filter = ('title', 'page_type', 'pubdate')
    exclude = ('updated',)


class MicroBlogAdmin(auto_update):
    list_display = ('description',)
    list_filter = ('pubdate',)
    exclude = ('html_text', 'updated')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Micro_blog, MicroBlogAdmin)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(PageCategories)
admin.site.register(Pages, PagesAdmin)
