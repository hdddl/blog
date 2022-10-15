from django.db import models


# Create your models here.

class KindNotes(models.Model):
    refresh_date = models.DateTimeField(verbose_name="生成时间", auto_now=True)
    content = models.TextField(verbose_name="剪切板内容")


# 书籍
class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name="书名")
    author = models.CharField(max_length=20, verbose_name="作者")
    note_nums = models.IntegerField(verbose_name="笔记条数")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "书籍"
        verbose_name_plural = "书籍"


# 标注
class Notes(models.Model):
    book_name = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="书名")
    content = models.TextField(verbose_name="内容")
    note_time = models.CharField(max_length=50, verbose_name="添加时间")
    note_location = models.CharField(max_length=30, verbose_name="添加位置")

    def __str__(self):
        return str(self.note_time) + ": " + str(self.note_location)

    class Meta:
        verbose_name = "标注"
        verbose_name_plural = "标注"
