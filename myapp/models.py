from django.db import models


class Device(models.Model):
    device_id = models.IntegerField(primary_key=True)
    device_name = models.CharField(max_length=100)
    device_manufacturer = models.CharField(max_length=100)

