from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description')

        labels = {
            'name': '',
            'description': '',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}), 
        }