from __future__ import unicode_literals

from django.db import models

# Create your models here.
# create table
class Post(models.Model) : 
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    
    