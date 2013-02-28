from django.db import models

class Message (models.Model):  
    Pseudo = models.CharField(max_length=128, null=True, blank=True)
    Description = models.CharField(max_length=256, null=True, blank=True)
    Message =  models.TextField(null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)