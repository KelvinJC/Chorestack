from django.forms import ModelForm
from .models import Bug


class BugForm(ModelForm):
    class Meta:
        model = Bug
        fields= ['name', 'project', 'error_message', 'description', 'resolution']
