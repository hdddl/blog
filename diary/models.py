from django.db import models


# Create your models here.

class Diary(models.Model):
    markdown_text = models.TextField(verbose_name="日记内容 MarkDown")
    html_text = models.TextField(verbose_name="日记内容 HTML")
    desc = models.CharField(max_length=100, verbose_name="描述", default=" ", blank=True)
    pubDate = models.DateField(verbose_name="日记时间")

    def __str__(self):
        return str(self.pubDate)
    class Meta:
        verbose_name_plural = "日记"

