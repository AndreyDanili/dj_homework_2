from django.db import models
from django.utils import timezone


class Sensor(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(max_length=None, blank=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement', default='')
