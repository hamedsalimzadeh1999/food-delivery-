from django.db import models
from django.utils import timezone
import uuid
from .main import Draft_publish
from .Coupon import Coupon
from django.contrib.auth.models import User
class Order(Draft_publish):
    orderingid = models.UUIDField(primary_key= True , default= uuid.uuid4 , editable=False)
    orderitems = models.ManyToManyField(User)
    price = models.PositiveIntegerField()
    coupon = models.OneToOneField(Coupon , on_delete=models.CASCADE)
    payment_List = (('O','online'),('C','Cash'))
    payment = models.CharField(choices = payment_List, max_length=3)

