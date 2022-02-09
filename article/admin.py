from django.contrib import admin

from .models import Blog, Micro_blog, Categories, Tags, Pages


# Register your models here.
class auto_update(admin.ModelAdmin):
    # ÷ÿ–¥save_model
    def save_model(self, request, obj, form, change):
        obj.updated = False
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
