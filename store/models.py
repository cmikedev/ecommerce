from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class photos(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')


class Customer(models.Model):
    name = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)