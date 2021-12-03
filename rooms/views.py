from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Room
from .forms import RoomForm


class RoomView(CreateView):
    model = Room
    template_name = "rooms/room.html"
    form_class = RoomForm
    success_url = reverse_lazy("room-done")


class RoomDoneView(TemplateView):
    template_name = "rooms/room_done.html"
