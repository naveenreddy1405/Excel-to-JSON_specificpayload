from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Select Excel file (.xlsx)")
