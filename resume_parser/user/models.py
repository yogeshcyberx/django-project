# from django.db import models
from djongo import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.IntegerField(null=True, blank=True)
    file = models.FileField(upload_to='resume/')
    date = models.DateTimeField(auto_now_add=True)