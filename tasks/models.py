from django.db import models

# Create your models here.
class Task(models.Model):
    tasks = models.CharField(max_length=50)
    important = models.BooleanField(default= False)
    complete = models.BooleanField(default= False)
