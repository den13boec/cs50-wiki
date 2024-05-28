from django.urls import path

from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    path("wiki/<slug:entry_title>", views.entry, name = "entry")
]
