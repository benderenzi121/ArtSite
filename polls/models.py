from django.db import models

# Create your models here.
class Poll(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    CHOICES = ( 'A' , 'Choice A' ),  ('B' , 'Choice b' ), ('C', 'Choice c' )
    vote = models.CharField(max_length=1, choices=CHOICES)
    
    
