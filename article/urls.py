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
    path("api/content", views.api_content, name="content"),
    path("api/categories", views.api_categories, name="categories"),
    path("api/tags", views.api_tags, name="tags"),
    path("api/pages", views.api_pages, name="pages"),
    path("rss/blog", rss.LatestBlogsFeed(), name="rss_blog"),
    path("rss/microBlog", rss.LatestMicroBlogFeed(), name="rss_microBlog")
]