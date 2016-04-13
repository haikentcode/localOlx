from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from datetime import datetime

from string import join
import os
import uuid

Image_Folder="media/"
# Create your models here.

class User(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    emailId=models.EmailField(blank=False,null=False,primary_key=True)
    contactNo=models.CharField(max_length=10)
    cityName=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    dateOfBirth=models.DateField(blank=True,null=True)

    def __str__(self):
        return "%s %s %s"%(self.firstName,self.lastName,self.emailId)

    class Admin:
        pass


class  Item(models.Model):
       name=models.CharField(max_length=100)
       image=models.ImageField(upload_to=Image_Folder)
       price=models.IntegerField(blank=True,null=True)
       info=models.CharField(max_length=500)
       user=models.ForeignKey(User)
       status=models.CharField(max_length=10)
       date=models.DateField(blank=True,null=True)


       def __str__(self):
           return self.name

       def image_tag(self):
          #--hkcheck--flag .. "/media/" use var
          return u'<img src="/media/%s" width="100px" height="100px"/>' % self.image
       image_tag.short_description = 'Item Image'
       image_tag.allow_tags = True