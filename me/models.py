from django.db import models

# Create your models here.

class skills(models.Model):
    title = models.CharField(max_length=200 ,null=True,blank=True)
    darsad = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.title


class favmusic(models.Model):
    title = models.CharField(max_length=200 , null=True,blank=True)
    image = models.ImageField(upload_to = '%Y/%m/%d' , null=True,blank=True)
    def __str__(self):
        return self.title

class favmovie(models.Model):
    title = models.CharField(max_length=200 , null=True,blank=True)
    image = models.ImageField(upload_to = '%Y/%m/%d' , null=True,blank=True)
    def __str__(self):
        return self.title
    