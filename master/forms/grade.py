from django import forms

from ..models.grade import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['retirement_date'].disabled = True

class GradeSearchForm(forms.Form):
    keyword = forms.fields.CharField(
        label = 'キーワード検索',
        required = False,
        widget=forms.widgets.TextInput,
    )

class GradeImportForm(forms.Form):
    upload_file = forms.fields.FileField(
        label = 'アップロードファイル',
        required = True,
        widget=forms.widgets.FileInput,
    )
