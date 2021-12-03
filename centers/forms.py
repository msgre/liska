from django import forms
from .models import Center


class CenterForm(forms.ModelForm):
    agreement = forms.BooleanField(label="Souhlasím se zpracováním dat dle Zásad ochrany osobních údajů zveřejněných zde na webu", initial=False)
    class Meta:
        model = Center
        fields = [
            'first_name', 
            'last_name', 
            'competence', 
            'region', 
            'email', 
            'phone', 
        ]
        widgets = {
            'competence': forms.RadioSelect,
        }
