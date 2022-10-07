from django import forms

class BugForm(forms.Form):
    name = forms.CharField(max_length = 100)