from django.db import models
from django.conf import settings

class Retailer(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=False)
    last_name =  models.CharField(max_length=255, null=True, blank=False)
