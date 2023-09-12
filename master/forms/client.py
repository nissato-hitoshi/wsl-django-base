from django import forms

from ..models.client import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ClientSearchForm(forms.Form):
    keyword = forms.fields.CharField(
        label = 'キーワード検索',
        required = False,
        widget=forms.widgets.TextInput,
    )

class ClientImportForm(forms.Form):
    upload_file = forms.fields.FileField(
        label = 'アップロードファイル',
        required = True,
        widget=forms.widgets.FileInput,
    )
