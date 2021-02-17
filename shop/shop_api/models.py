from django.db import models
from django.conf import settings


class Shop(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    address =  models.CharField(max_length=255, null=True, blank=False)
    retailer_id = models.PositiveIntegerField(null=True, blank=False)
