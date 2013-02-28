from django.db import models

class Message (models.Model):  
    Pseudo = models.CharField(max_length=128, null=True, blank=True)
    Description = models.CharField(max_length=256, null=True, blank=True)
    Message =  models.TextField(null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):  
          return "%s %s" % (self.id,self.Description)

class Configuration (models.Model):  
    NbreMessage = models.IntegerField(null=True, blank=True)
    def __str__(self):  
          return "%s %s" % (str(self.id),str(self.NbreMessage))