from.models import student
from django import forms
class nextform(forms.ModelForm):
    class Meta:
        model=next
        fields='--all--'