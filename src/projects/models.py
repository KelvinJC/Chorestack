from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    name = models.CharField('Project name', max_length=50)
    time_created = models.DateTimeField(default=timezone.now) # time info is entered into the system. May not reflect actual start of project
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
