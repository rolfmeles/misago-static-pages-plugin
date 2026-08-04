# misago_static_pages_plugin/views.py

from django.shortcuts import get_object_or_404, render

from .models import StaticPage


def static_page(request, slug):
    page = get_object_or_404(
        StaticPage,
        slug=slug,
    )

    return render(
        request,
        "misago_static_pages_plugin/static_page.html",  # main template for the final page
        {
            "page": page,
        },
    )
