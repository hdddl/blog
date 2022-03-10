from django.db import models


# Create your models here.
class TimeStampMixin(models.Model):
    pubdate = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 博客tags
class Tags(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name


# 博客分类
class Categories(models.Model):
    name = models.CharField(max_length=50, default='未分类')

    class Meta:
        ordering = ['name']
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name


class Blog(TimeStampMixin):
    # 文章标题
    title = models.CharField(max_length=50, unique=True)
    # 文章作者
    author = models.CharField(max_length=50, default='Dongliu')
    # 访问次数
    visits = models.BigIntegerField(default=0)
    # 文章摘要
    abstract = models.TextField(null=True)
    # markdown文章正文
    markdown_text = models.TextField(default=' ')
    # html文章正文
    html_text = models.TextField(null=True, blank=True)
    # 文章分类
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    # 文章标签(多对多关系)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pubdate']  # 按照发布时间排序
        verbose_name_plural = "博客"


class Micro_blog(TimeStampMixin):
    # markdown文章正文
    markdown_text = models.TextField()
    # html文章正文
    html_text = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-pubdate']
        verbose_name_plural = "微博"

    def __str__(self):
        return str(self.pubdate)


# 一些特殊页面
class Pages(TimeStampMixin):
    name = models.CharField(max_length=20, unique=True)
    # markdown文章正文
    markdown_text = models.TextField(null=True, blank=True)
    # html文章正文
    html_text = models.TextField(null=True, blank=True)

    text_type = models.CharField(max_length=20, default='markdown')

    class Meta:
        verbose_name_plural = "特殊页面"

    def __str__(self):
        return self.name
