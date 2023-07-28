from django import forms
from . import models

class CsvForm(forms.ModelForm):
    class Meta:
        model = models.Csv
        fields=['file_name', 'activated']