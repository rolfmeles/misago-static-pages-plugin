# misago-static-pages-plugin/misago_static_pages_plugin/urls.py

from django.urls import path

from . import views


urlpatterns = [
    path(
        "pages/<slug:slug>/",
        views.static_page,
        name="static-page",
    ),
]
