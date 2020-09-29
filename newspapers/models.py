from django.db import models
from django.utils import timezone

class Forecast(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    main = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    temperatue = models.CharField(max_length=150)
    wind = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

