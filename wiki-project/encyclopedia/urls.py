from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("wiki/<slug:entry_title>/", views.entry, name = "entry"),
    path("search_article/", views.search_entry, name = "search_entry"),
    path("new_page/", views.new_page, name = "new_page"),
    path("random_page/", views.random_page, name = "random_page"),
    path("", views.index, name="index"),
]
