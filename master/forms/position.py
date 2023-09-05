from django import forms

from ..models.position import Position

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['retirement_date'].disabled = True

