from django.db import models
from django.db.models.fields import AutoField

# Create your models here.

class blogposts(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(blank=True , null=True)
    date = models.DateField(auto_now=True)
    isfav = models.BooleanField(blank=True , null=True)
    image = models.ImageField(upload_to = '%Y/%m/%d' , null=True,blank=True)
    def __str__(self):
        return self.title