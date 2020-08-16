from django.db import models
from django.utils import timezone
import uuid
from .main import Draft_publish
from .Orderingitems import Order
from django.contrib.auth.models import User
from django.conf import settings
class User(Draft_publish):
    UserId = models.UUIDField(primary_key= True , default= uuid.uuid4 , editable=False)
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    addres = models.TextField()
    published_at = models.DateTimeField(default = timezone.now)
    email = models.EmailField()
    birthday = models.DateField(null = True , blank = True)
    orderingList = models.ManyToManyField(Order)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-published_at']
    def __str__(self):
        return self.name
    def __unicode__(self):
        return u"%s" % self.user