from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Room
from .resources import RoomResource


class RoomAdmin(ImportExportModelAdmin):
    list_display = ('vat', 'capacity',)
    search_fields = ['vat', 'phone']
    resource_class = RoomResource


admin.site.register(Room, RoomAdmin)
