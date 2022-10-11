from django.db import models
from django.utils import timezone
from projects.models import Project


# Create your models here.


class Bug(models.Model):
    name = models.CharField('Bug name', max_length=100)
    project = models.ForeignKey(Project, max_length=50, null=True, on_delete=models.SET_NULL)
    time_reported = models.DateTimeField(default=timezone.now)
    time_resolved = models.DateTimeField(blank=True, null=True)
    # timedelta in days or hours between creation and resolution
    is_active = models.BooleanField(default=True)
    error_message = models.TextField('Error message', blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    resolution = models.TextField('Resolution', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

'''
research tagging models further e.g django taggit

class Tag(models.Model):
    name = models.CharField('Tag', max_length=20)
    def __str__(self) -> str:
        return self.name
'''
