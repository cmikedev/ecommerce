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


class Contact(models.Model):
    question_type = (
        ("licence", "Licence Type"),
        ("maintenance", "Maintenance"),
        ("sales", "Sales"),
        ("shipping_charges", "Shipping Charges"),
        ("refunds_returns", "Refunds and Returns"),
        ("warranty", "Warranty Queries"),
        ("other", "Other Queries"),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    question_categories = models.CharField('What does your query relate to?', max_length=50, choices=question_type, default='certification')
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.email
