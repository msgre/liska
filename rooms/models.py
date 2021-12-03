from django.db import models
from django_extensions.db.models import TimeStampedModel


class Room(TimeStampedModel):
    vat = models.CharField("Vaše IČO", max_length=255)
    capacity = models.IntegerField("Kapacita", default=10, help_text="Zadejte počet vakcinací, které za týden zvládnete")
    day_monday = models.BooleanField("Pondělí", default=True)
    day_tuesday = models.BooleanField("Úterý", default=True)
    day_wednesday = models.BooleanField("Středa", default=True)
    day_thursday = models.BooleanField("Čtvrtek", default=True)
    day_friday = models.BooleanField("Pátek", default=True)
    day_sathurday = models.BooleanField("Sobota", default=False)
    day_sunday = models.BooleanField("Neděle", default=False)
    phone = models.CharField("Telefonní kontakt", max_length=50)

    class Meta:
        verbose_name = "Ordinace"
        verbose_name_plural = "Ordinace"

    def __str__(self):
        return self.vat
