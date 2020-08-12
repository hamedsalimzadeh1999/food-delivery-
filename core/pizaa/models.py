from django.db import models
from uuid import uuid4
# Create your models here.
class pizza (models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField()
    price = models.PositiveIntegerField()

class Customer(models.Model):
    Customerid = models.AutoField(primary_key=True)
    PhoneNumber = models.PositiveIntegerField()
    addres = models.CharField(max_length=50)
class ordermodel(models.Model):
    username = models.CharField(max_length=50)
    pnonenumber = models.PositiveIntegerField()
    address = models.TextField(max_length=50)
    ordertime = models.DateTimeField(auto_now_add=True)
    ordereditems = models.CharField(max_length = 10)

