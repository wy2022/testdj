from django.db import models

# Create your models here.

class user(models.Model):
    user = models.CharField(max_length=20)
    email = models.EmailField()