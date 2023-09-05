from django import forms

from ..models.affiliation import Affiliation

class AffiliationForm(forms.ModelForm):
    class Meta:
        model = Affiliation
        fields = '__all__'
        widgets = {
            'start_date': forms.NumberInput(attrs={ "type": "date" }),
            'end_date': forms.NumberInput(attrs={ "type": "date" }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

