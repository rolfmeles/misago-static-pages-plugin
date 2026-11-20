from django.urls import path

from . import views

urlpatterns = [
    path(
        "pages/<slug:slug>/",
        views.static_page,
        name="static-page",
    ),
]
