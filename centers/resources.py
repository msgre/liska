from import_export import resources
from .models import Center


class CenterResource(resources.ModelResource):
    class Meta:
        model = Center
