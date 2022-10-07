from django.db import models
from django.utils import timezone

# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100)
    project = models.CharField(max_length=50)
    time_created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)