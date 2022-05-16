from django.urls import path
from . import views
from . import rss

urlpatterns = [
    path("", views.index_page, name="index"),
    path("blog", views.blog_article_page, name="blog_article"),
    path("micro_blog", views.micro_blog_page, name="micro_blog"),
    path("about", views.about_page, name="about"),
    path("tags", views.tags_page, name='tag'),
    path("categories", views.category_page, name="category"),
    path("api/pages", views.api_pages, name="pages"),
    path("feed/blog", rss.LatestBlogsFeed(), name="rss_blog"),
    path("feed/microBlog", rss.LatestMicroBlogFeed(), name="rss_microBlog")
]