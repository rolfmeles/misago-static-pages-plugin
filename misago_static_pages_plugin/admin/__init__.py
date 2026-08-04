# misago_static_pages_plugin/admin/__init__.py

from django.urls import path
from django.utils.translation import pgettext_lazy

from .views import PagesList, NewPage, EditPage, DeletePage


class MisagoAdminExtension:
    def register_urlpatterns(self, urlpatterns):
        # Static Pages section
        urlpatterns.namespace("staticpages/", "staticpages")

        # Pages
        urlpatterns.patterns(
            "staticpages",
            path("", PagesList.as_view(), name="index"),
            path("new/", NewPage.as_view(), name="new"),
            path("edit/<int:pk>/", EditPage.as_view(), name="edit"),
            path("delete/<int:pk>/", DeletePage.as_view(), name="delete"),
        )

    def register_navigation_nodes(self, site):
        site.add_node(
            name=pgettext_lazy("mspp", "Static Pages"),
            icon="fa fa-file-alt",
            after="plugins:index",
            namespace="staticpages",
        )
