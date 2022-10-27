from django.db import models
from django.conf import settings


# Create your models here.
class Hero(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  hero = models.OneToOneField(Hero, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

