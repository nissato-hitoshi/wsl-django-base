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

class AccountingPeriodSearchForm(forms.Form):
    keyword = forms.fields.CharField(
        label = 'キーワード検索',
        required = False,
        widget=forms.widgets.TextInput,
    )

class AccountingPeriodImportForm(forms.Form):
    upload_file = forms.fields.FileField(
        label = 'アップロードファイル',
        required = True,
        widget=forms.widgets.FileInput,
    )
