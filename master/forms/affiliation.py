from django import forms

from ..models.affiliation import Affiliation
from ..models.accounting_period import AccountingPeriod

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

class AffiliationSearchForm(forms.Form):
    search_accounting_period = forms.ModelChoiceField(
        queryset=AccountingPeriod.objects.all(),
        label = '会計期',
        required = False,
    )
    keyword = forms.fields.CharField(
        label = 'キーワード検索',
        required = False,
        widget=forms.widgets.TextInput,
    )

class AffiliationImportForm(forms.Form):
    upload_file = forms.fields.FileField(
        label = 'アップロードファイル',
        required = True,
        widget=forms.widgets.FileInput,
    )
