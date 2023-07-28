from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)