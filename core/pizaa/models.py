from django.db import models
from uuid import uuid4
# Create your models here.
class pizza (models.Model):
    uuid = models.UUIDField(primary_key=True ,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=50)
    info = models.TextField()
    price = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
        class class Meta:
        db_table = ''
        managed = True
        ordering=['-created']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    Customerid = models.UUIDField(primary_key=True ,default=uuid.uuid4,editable=False)
    
    PhoneNumber = models.PositiveIntegerField()
    addres =models.CharField()
    class class Meta:
        db_table = ''
        managed = True
        ordering=[-'']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
