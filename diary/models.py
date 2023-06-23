from django.db import models


# Create your models here.

class Diary(models.Model):
    markdown_text = models.TextField(verbose_name="日记内容 MarkDown")
    html_text = models.TextField(verbose_name="日记内容 HTML")
    pubData = models.DateField(verbose_name="日记时间")
