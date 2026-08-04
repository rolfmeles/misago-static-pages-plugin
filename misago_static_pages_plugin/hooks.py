# misago_static_pages_plugin/hooks.py

def register_static_pages_urls(urlpatterns):
    from django.urls import path
    from .views import static_page
    from .urls import urlpatterns
