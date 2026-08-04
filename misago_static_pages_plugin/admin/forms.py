# misago_static_pages_plugin/admin/forms.py

from django import forms
from django.utils.translation import pgettext_lazy

from ..models import StaticPage


class PageForm(forms.ModelForm):
    title = forms.CharField(label=pgettext_lazy("mspp", "Title"))
    slug = forms.CharField(label=pgettext_lazy("mspp", "Slug"))
    content = forms.CharField(label=pgettext_lazy("mspp", "Content"))

    class Meta:
        model = StaticPage
        fields = [
            "title",
            "slug",
            "content",
        ]
