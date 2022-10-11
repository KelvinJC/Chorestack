from django.forms import ModelForm
from django import forms
from .models import Bug



class BugForm(ModelForm):
    class Meta:
        model = Bug
        fields= ['name', 'project', 'error_message', 'description']
        
        labels = {

            'name': '',
            'project': '',
            'error_message': '',
            'description': '',
            
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'project': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Project'}),
            'error_message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Error message'}),
            'description': forms.Textarea(attrs={'class': 'form-control',  'placeholder': 'Description'}),

        }


class BugResolutionForm(ModelForm):
    class Meta:
        model = Bug
        fields= ['name', 'project', 'error_message', 'description', 'resolution']
        
        labels = {

            'name': '',
            'project': '',
            'error_message': '',
            'description': '',
            'resolution': '',
            
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'project': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Project'}),
            'error_message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Error message'}),
            'description': forms.Textarea(attrs={'class': 'form-control',  'placeholder': 'Description'}),
            'resolution': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Resolution'})

        }

