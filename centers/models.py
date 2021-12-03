from django.db import models
from django_extensions.db.models import TimeStampedModel


class Center(TimeStampedModel):
    COMPETENCE_LEKAR = 'lekar'
    COMPETENCE_DOBROVOLNIK_NEZDRAVOTNIK = 'dobrovolnik_nezdravotnik'
    COMPETENCE_CHOICES = (
        (COMPETENCE_LEKAR, 'Lékař'),
        (COMPETENCE_DOBROVOLNIK_NEZDRAVOTNIK, 'Dobrovolník nezdravotník'),
    )

    REGION_PHA = 'PHA'
    REGION_STC = 'STC'
    REGION_JHC = 'JHC'
    REGION_PLK = 'PLK'
    REGION_KVK = 'KVK'
    REGION_ULK = 'ULK'
    REGION_LBK = 'LBK'
    REGION_HKK = 'HKK'
    REGION_PAK = 'PAK'
    REGION_VYS = 'VYS'
    REGION_JHM = 'JHM'
    REGION_OLK = 'OLK'
    REGION_MSK = 'MSK'
    REGION_ZLK = 'ZLK'
    REGION_CHOICES = (
        (REGION_PHA, 'Hlavní město Praha'),
        (REGION_STC, 'Středočeský kraj'),
        (REGION_JHC, 'Jihočeský kraj'),
        (REGION_PLK, 'Plzeňský kraj'),
        (REGION_KVK, 'Karlovarský kraj'),
        (REGION_ULK, 'Ústecký kraj'),
        (REGION_LBK, 'Liberecký kraj'),
        (REGION_HKK, 'Královéhradecký kraj'),
        (REGION_PAK, 'Pardubický kraj'),
        (REGION_VYS, 'Kraj Vysočina'),
        (REGION_JHM, 'Jihomoravský kraj'),
        (REGION_OLK, 'Olomoucký kraj'),
        (REGION_MSK, 'Moravskoslezský kraj'),
        (REGION_ZLK, 'Zlínský kraj'),
    )

    first_name = models.CharField("Jméno", max_length=255)
    last_name = models.CharField("Příjmení", max_length=255)
    competence = models.CharField("Kompetence", max_length=50, choices=COMPETENCE_CHOICES, blank=False, default="")
    region = models.CharField("Kraj", max_length=100, choices=REGION_CHOICES)
    email = models.EmailField("Email")
    phone = models.CharField("Mobil", max_length=50)

    class Meta:
        verbose_name = "Existujicí místo"
        verbose_name_plural = "Existujicí místa"

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.get_region_display()})'
