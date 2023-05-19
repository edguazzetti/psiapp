from django.db import models

# Create your models here.

class Planes(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=0, blank=False, null=False)