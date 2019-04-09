from django import forms
from .models import Githuber

class GithuberForm(forms.ModelForm):
    class Meta:
        model = Githuber
        fields = '__all__'