from django.db import models


# Create your models here.

class blog(models.Model):
    # 文章标题
    title = models.CharField(max_length=50, unique=True)
    # 文章作者
    author = models.CharField(max_length=50, default='Dongliu')
    # 访问次数
    visits = models.BigIntegerField(default=0)
    # 文章摘要
    abstract = models.TextField(null=True)
    # 文章正文
    content = models.TextField()
    # 文章发布时间
    pubdate = models.DateTimeField()
    # 文章修改时间
    modify_date = models.DateTimeField()
    # 文章分类
    category = models.CharField(max_length=50, null=True)
    # 文章标签
    tags = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title


class micro_blog(models.Model):
    # 发布时间
    pubdate = models.DateField()
    # 发布内容
    content = models.TextField()

    def __str__(self):
        return self.pubdate
