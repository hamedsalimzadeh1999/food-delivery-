  
from django.db import models
from .main import Draft_publish
class Coupon(models.Model):
    tittle = models.CharField(max_length=256, db_index=True, unique=True)
    info = models.TextField()
    slug  = models.SlugField(max_length=128,unique=True)
    auth_time = models.IntegerField(null=False)
    def __str__(self):
        return self.tittle
    def is_expired(self):
        return self.auth_time + 300 < time.time()
    def get_auth_time(self):
        return self.auth_time