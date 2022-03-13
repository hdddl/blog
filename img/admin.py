from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Image, Album
from blog.env import HOST


# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "album", "pubdate")
    list_filter = ("album", )
    readonly_fields = ("image_preview",)

    @admin.display(description="preview")
    def image_preview(self, instance):
        """
        展示图片预览
        """
        url = HOST + "/media" +  instance.image.url
        return mark_safe('<img src="%s" style="width: 30%; height: 17%">'%url)


admin.site.register(Image, ImageAdmin)
admin.site.register(Album)
