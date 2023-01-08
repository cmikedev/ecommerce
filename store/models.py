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

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, unique=True)
    manufacturer = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField(max_length=1000)
    price = models.FloatField()
