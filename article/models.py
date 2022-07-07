from django.db import models


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


class Blog(models.Model):
    private = models.BooleanField()     # 是否为仅仅自己可见
    pubdate = models.DateTimeField(auto_now_add=True)  # 文章发布时间
    modify_date = models.DateTimeField(auto_now=True)  # 最近一次文章修改时间
    title = models.CharField(max_length=50, unique=True)  # 文章标题
    author = models.CharField(max_length=50, default='Dongliu')  # 文章作者
    visits = models.BigIntegerField(default=0)  # 访问次数
    abstract = models.TextField(null=True)  # 文章摘要
    markdown_text = models.TextField(default=' ')  # markdown文章正文
    html_text = models.TextField(null=True, blank=True)  # html文章正文
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)  # 文章分类
    tags = models.ManyToManyField(Tags)  # 文章标签(多对多关系)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pubdate']  # 按照发布时间排序
        verbose_name_plural = "博客"


class Micro_blog(models.Model):
    private = models.BooleanField()  # 是否为仅仅自己可见
    pubdate = models.DateTimeField(auto_now_add=True)  # 文章发布时间
    modify_date = models.DateTimeField(auto_now=True)  # 最近一次文章修改时间
    markdown_text = models.TextField()  # markdown文章正文
    html_text = models.TextField(null=True, blank=True)  # html文章正文
    description = models.CharField(max_length=50, default="blank")

    class Meta:
        ordering = ['-pubdate']
        verbose_name_plural = "微博"

    def __str__(self):
        return self.description


class PageCategories(models.Model):
    name = models.CharField(max_length=20, default='markdown')

    class Meta:
        verbose_name_plural = "页面类型"

    def __str__(self):
        return self.name


# 一些特殊页面
class Pages(models.Model):
    pubdate = models.DateTimeField(auto_now_add=True)  # 文章发布时间
    modify_date = models.DateTimeField(auto_now=True)  # 最近一次文章修改时间
    title = models.CharField(max_length=20, unique=True)
    markdown_text = models.TextField(null=True, blank=True)  # markdown文章正文
    html_text = models.TextField(null=True, blank=True)  # html文章正文
    page_type = models.ForeignKey(PageCategories, on_delete=models.CASCADE)     # 页面类型

    class Meta:
        verbose_name_plural = "特殊页面"

    def __str__(self):
        return self.title
