from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/content", views.api_content, name="content"),
    path("api/blog", views.api_blog, name="article"),
    path("api/categories", views.api_categories, name="categories"),
    path("api/tags", views.api_tags, name="tags")
]