from django.urls import path
from reading import views


urlpatterns = [
    path("", views.book_index, name= "index"),
    path("notes", views.book_notes, name="notes")
]