from import_export import resources
from .models import Room


class RoomResource(resources.ModelResource):
    class Meta:
        model = Room
