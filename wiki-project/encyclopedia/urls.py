from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("wiki/<slug:entry_title>/", views.entry, name = "entry"),
    path("wiki/", views.index, name="index"),
]
