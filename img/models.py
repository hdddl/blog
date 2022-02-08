# coding=utf-8
from django.db import models


# Create your models here.
# 相册
class Album(models.Model):
    # 相册名称
    name = models.CharField(default='未分类', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "相册"


# 图片信息
class Image(models.Model):
    # 图片名
    name = models.CharField(max_length=50)
    # 相册名
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # 添加时间
    pubdate = models.DateTimeField(auto_now_add=True)
    # 图片
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "图片"
        ordering = ['name']
