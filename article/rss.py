# coding=utf-8
# 为我的博客创建RSS
from django.contrib.syndication.views import Feed
from article.models import Blog, Micro_blog


def items():
    return Blog.objects.order_by("-pubdate")[:5]


class LatestBlogsFeed(Feed):
    """
    最近的五条博客
    """
    title = "东流的Blog"
    link = "/"
    description = "青山遮不住，毕竟东流去。"
    def items(self):
        return Blog.objects.order_by("-pubdate")[0:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.html_text

    def item_link(self, item):
        return "/blog?title=" + item.title


class LatestMicroBlogFeed(Feed):
    """
    最近几条微博
    """
    title = "东流的微博"
    link = "/micro_blog"
    description = "一些胡言乱语罢了"

    def items(self):
        return Micro_blog.objects.order_by("-pubdate")[0:5]

    def item_title(self, item):
        return item.pubdate  # 因为微博没有title就用时间来代替了

    def item_description(self, item):
        return item.html_text

    def item_link(self, item):
        return self.link        # 因为每篇微博没有单独的链接所以就只能返回整体链接了
