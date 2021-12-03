from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Center
from .resources import CenterResource


class CenterAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'competence', 'region')
    list_filter = ('competence', 'region')
    search_fields = ['email', 'last_name', 'first_name', 'phone']
    resource_class = CenterResource


admin.site.register(Center, CenterAdmin)
