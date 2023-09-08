from django import forms

from ..models.accounting_period import AccountingPeriod

class AccountingPeriodForm(forms.ModelForm):
    class Meta:
        model = AccountingPeriod
        fields = '__all__'
        widgets = {
            'start_date': forms.NumberInput(attrs={ "type": "date" }),
            'end_date': forms.NumberInput(attrs={ "type": "date" }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

