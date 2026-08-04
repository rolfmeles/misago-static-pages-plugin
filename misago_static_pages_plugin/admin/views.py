# misago_static_pages_plugin/admin/views.py

from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import pgettext_lazy

from ..models import StaticPage
from misago.admin.views import generic
from .forms import PageForm


class PagesAdmin(generic.AdminBaseMixin):
    root_link = "misago:admin:staticpages:index"
    model = StaticPage
    templates_dir = "misago_static_pages_plugin/admin"
    message_404 = pgettext_lazy("mspp", "Requested page does not exist.")


class PagesList(PagesAdmin, generic.ListView):
    ordering = (("title", None),)


class PageFormMixin:
    def real_dispatch(self, request, target):
        form = PageForm(instance=target)

        if request.method == "POST":
            form = PageForm(request.POST, instance=target)
            if form.is_valid():
                form.instance.save()

                messages.success(request, self.message_submit % {"title": target.title})

                if "stay" in request.POST:
                    return redirect(request.path_info)
                return redirect(self.root_link)
            else:
                form.add_error(
                    None, pgettext_lazy("admin form", "Form contains errors.")
                )

        template_name = self.get_template_name(request, target)
        return self.render(
            request,
            {
                "form": form,
                "target": target,
            },
            template_name,
        )


class NewPage(PageFormMixin, PagesAdmin, generic.ModelFormView):
    message_submit = pgettext_lazy("mspp", 'New page "%(title)s" has been saved.')


class EditPage(PageFormMixin, PagesAdmin, generic.ModelFormView):
    message_submit = pgettext_lazy("mspp", 'Page "%(title)s" has been changed.')


class DeletePage(PagesAdmin, generic.ButtonView):
    def button_action(self, request, target):
        target.delete()
        message = pgettext_lazy("mspp", 'Page "%(title)s" has been deleted.')
        messages.success(request, message % {"title": target.title})
