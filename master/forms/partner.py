from django import forms

from ..models import Partner

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PartnerSearchForm(forms.Form):
    keyword = forms.fields.CharField(
        label = 'キーワード検索',
        required = False,
        widget=forms.widgets.TextInput,
    )

class PartnerImportForm(forms.Form):
    upload_file = forms.fields.FileField(
        label = 'アップロードファイル',
        required = True,
        widget=forms.widgets.FileInput,
    )
