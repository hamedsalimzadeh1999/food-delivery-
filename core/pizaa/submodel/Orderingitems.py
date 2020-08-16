from django.db import models
from django.utils import timezone
import uuid
from .main import Draft_publish
from .User import User
from .Coupon import Coupon
from django.contrib.auth.models import User
class Order(Draft_publish):
    orderingid = models.UUIDField(primary_key= True , default= uuid.uuid4 , editable=False)
    orderitems = models.ManyToManyField(User)
    price = models.PositiveIntegerField()
    coupon = models.OneToOneField(Coupon)
    payment_List = (('O','online'),('C','Cash'))
    payment = MultiSelectField(choices = Auther_LIST, max_length=3)

