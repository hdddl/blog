from django.urls import path
from . import views

urlpatterns = [
    path("", views.diary_index, name="index"),
    path("diary", views.diary_context, name="context")
]