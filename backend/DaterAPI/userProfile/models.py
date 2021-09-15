from django.db import models

# Create your models here.


"""User model"""


class User(models.Model):
    phone = models.CharField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)
