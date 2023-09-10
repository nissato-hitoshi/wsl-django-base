from django import forms

from ..models.employee import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.NumberInput(attrs={ "type": "date" }),
            'hire_date': forms.NumberInput(attrs={ "type": "date" }),
            'retirement_date': forms.NumberInput(attrs={ "type": "date" }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EmployeeSearchForm(forms.Form):
    keyword = forms.fields.CharField(
        label = 'キーワード検索',
        required = False,
        widget=forms.widgets.TextInput,
    )

class EmployeeImportForm(forms.Form):
    upload_file = forms.fields.FileField(
        label = 'アップロードファイル',
        required = True,
        widget=forms.widgets.FileInput,
    )
