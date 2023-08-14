from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    narx = models.FloatField(null=True, blank=True)
    turi = models.CharField(max_length=50, null=True, blank=True)
    miqdor = models.IntegerField(null=True, blank=True)
    administrator = models.CharField(max_length=30, null=True, blank=True)