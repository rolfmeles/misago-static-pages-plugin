# misago_static_pages_plugin/migrations/0001_initial.py

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StaticPage",
            fields=[
                (
                    "title",
                    models.CharField(
                        max_length=200,
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        unique=True,
                    ),
                ),
                (
                    "content",
                    models.TextField(),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        auto_now_add=True,
                    ),
                ),
                (
                    "updated_on",
                    models.DateTimeField(
                        auto_now=True,
                    ),
                ),
            ],
            options={
                "ordering": ["title"],
            },
        ),
    ]
