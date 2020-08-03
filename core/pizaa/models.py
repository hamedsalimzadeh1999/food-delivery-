from django.db import models

# Create your models here.
class pizza (models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField()
    price = models.PositiveIntegerField()