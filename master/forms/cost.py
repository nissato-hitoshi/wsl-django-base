from django import forms

from ..models.cost import Cost
from ..models.accounting_period import AccountingPeriod
from ..models.employee import Employee

class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CostSearchForm(forms.Form):
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

class CostImportForm(forms.Form):
    search_accounting_period = forms.ModelChoiceField(
        queryset=AccountingPeriod.objects.all(),
        label = '会計期',
        required = True,
    )
    upload_file = forms.fields.FileField(
        label = 'アップロードファイル',
        required = True,
        widget=forms.widgets.FileInput,
    )
