from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

from .models import Csv

class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)