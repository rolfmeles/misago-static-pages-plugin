# misago-static-pages-plugin/misago_static_pages_plugin/models.py

from django.db import models


class StaticPage(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    content = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
