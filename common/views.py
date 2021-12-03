from django.views.generic.base import TemplateView
from rooms.models import Room
from centers.models import Center


class HomePageView(TemplateView):
    template_name = "common/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_count'] = Center.objects.count() + Room.objects.count()
        return context


class HelpView(TemplateView):
    template_name = "common/help.html"
