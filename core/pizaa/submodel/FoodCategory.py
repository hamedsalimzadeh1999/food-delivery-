from django.db import models
from django.utils import timezone
import uuid
from .main import Draft_publish
class Food(Draft_publish):
    FoodId = models.UUIDField(primary_key= True , default= uuid.uuid4 , editable=False)
    name = models.CharField(max_length=128)
    published_at = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='post',blank=True, null=True , help_text='uplaod image',width_field='width_field', height_field='height_field')
    width_field  = models.PositiveIntegerField(null = True , blank = True , default = '1080')
    height_field = models.PositiveIntegerField(null = True , blank = True , default = '720')
    price= models.PositiveIntegerField()
    info = models.TextField()
    category = models.OneToOneField('pizaa.Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
    def Published_Food(self):
        return self.get_queryset().filter(publish_status = 'p').ordering_by('-published_at')
    def Deraft_Food(self):
        return self.get_queryset().filter(publish_status = 'd').ordering_by('-published_at')

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'