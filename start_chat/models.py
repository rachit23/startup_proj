from django.db import models

# Create your models here.

class Message(models.Model):
    body = models.CharField(max_length=300)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
