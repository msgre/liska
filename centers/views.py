from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Center
from .forms import CenterForm


class CenterView(CreateView):
    model = Center
    template_name = "centers/center.html"
    form_class = CenterForm
    success_url = reverse_lazy("center-done")


class CenterDoneView(TemplateView):
    template_name = "centers/center_done.html"
