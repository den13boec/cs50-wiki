from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("random_page/", views.random_page, name = "random_page"),
    path("search_article/", views.search_entry, name = "search_entry"),
    path("new_page/", views.new_page, name = "new_page"),
    path("wiki/<entry_title>/edit_page", views.edit_entry, name = "edit_page"),
    path("wiki/<entry_title>/", views.entry, name = "entry"),
    path("", views.index, name="index"),
]
