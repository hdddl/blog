from django.contrib import admin

from .models import Image, Album


# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "album", "pubdate")


admin.site.register(Image, ImageAdmin)
admin.site.register(Album)
