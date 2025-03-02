from django.db import models

# Create your models here.

class Password(models.Model):
    id = models.AutoField(primary_key=True)
    provider = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    link = models.CharField(max_length=100)