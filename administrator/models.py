from django.db import models

# Create your models here.
# create table, everything in the table is an object
class Post(models.Model) : 
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    
    
    #convert object into string
    def __str__(self) :
        return self.title

class User(models.Model) : 
    name = models.CharField(max_length = 140)
    pw = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    role = models.CharField(max_length = 10)
    expert = models.BooleanField(default=False)
    
    def __str__(self) :
        return self.name
        
class Topics(models.Model):
    topic = models.CharField(max_length = 200)
    date = models.DateTimeField()
    
    def __str__(self) :
        return self.topic
        
class Datasets(models.Model) :
    content = models.TextField();

class Curation(models.Model) :
    tid = models.
    