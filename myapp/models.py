

#Calendar
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image_url = models.TextField(null=True, blank=True)
    Bio = models.TextField(null=True, blank=True)
    
    
    class Meta:
        order_with_respect_to = 'name'

    def __str__(self): 
        return f"{self.name} {self.position} {self.company}"