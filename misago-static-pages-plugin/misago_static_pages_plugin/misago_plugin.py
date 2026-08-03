# misago_static_pages_plugin/misago_plugin.py
# The Misago Plugin Manifest File

from django.utils.encoding import force_str
from django.utils.translation import pgettext_lazy

from misago import MisagoPlugin


manifest = MisagoPlugin(
    name=force_str(pgettext_lazy("mspp", "Static Pages")),
    description=force_str(
        pgettext_lazy(
            "mspp",
            "Allows to create static pages in the admin panel, e.g. for information and ressources that don't need to be a forum thread.",
        )
    ),
    author="Rolf T. Meles",
    license="GPL-2.0",
    version="1.0",
    icon="fa fa-file-alt",
)
