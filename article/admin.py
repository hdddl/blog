from django.contrib import admin

from .models import Blog, Micro_blog, Categories, Tags, Pages

# Register your models here.

admin.site.register(Blog)
admin.site.register(Micro_blog)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Pages)
