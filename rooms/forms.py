from django import forms
from .models import Room


class RoomForm(forms.ModelForm):
    agreement = forms.BooleanField(label="Souhlasím se zpracováním dat dle Zásad ochrany osobních údajů zveřejněných zde na webu", initial=False)
    class Meta:
        model = Room
        fields = [
            'vat', 
            'capacity', 
            'day_monday', 
            'day_tuesday', 
            'day_wednesday', 
            'day_thursday', 
            'day_friday', 
            'day_sathurday', 
            'day_sunday', 
            'phone', 
        ]
