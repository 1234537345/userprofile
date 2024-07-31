from django.db import models
from django.db.models import CharField


class userprofile(models.Model):
    fullname=models.CharField(max_length=200)
    DOB=models.CharField(max_length=200)
    bio=models.CharField(max_length=200,blank=True, null=True)
    skills = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(max_length=255,blank=True, null=True)
    phone = models.CharField(max_length=10,blank=True, null=True)




def __str__(self):
    return '{}'.format(self.fullname)
