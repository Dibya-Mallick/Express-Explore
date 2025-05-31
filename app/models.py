from django.db import models
from datetime import datetime

# Create your models here.
class Options(models.Model):
    name= models.CharField(max_length=100)
    about= models.CharField(max_length=500)

class Blogs(models.Model):
    title= models.CharField(max_length=100)
    body= models.TextField()
    posted= models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title

class New(models.Model):
    title= models.CharField(max_length=200)
    owner=models.CharField(max_length=70)
    body= models.CharField(max_length=5000)
