from django.db import models

# Create your models here.

class UserDetails(models.Model):
    state = models.CharField(max_length=100,default='',null=False)
    emailid = models.CharField(max_length=100,default='',null=False)
    phoneno = models.CharField(max_length=100,default='',null=False)

