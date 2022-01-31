from django.contrib import admin

from .models import blog, micro_blog

# Register your models here.

admin.site.register(blog)
admin.site.register(micro_blog)
