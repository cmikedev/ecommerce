from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


class Photo(models.Model):
    """
    This is a custom model which allows for
    the uploading of photos to Cloudinary
    """
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title


class Customer(models.Model):
    """
    Model taken from Dennis Ivy's tutorial - see README.md
    """
    user = models.OneToOneField(
            User, null=True, blank=True, on_delete=models.CASCADE
        )
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return str(self.user)


class Product(models.Model):
    """
    This is a custom model with full front-end CRUD
    capability
    """
    licence_type = (
        ("a1", "A1"),
        ("a2", "A2"),
        ("a", "A"),
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, default="detail_view")
    manufacturer = models.CharField(max_length=200)
    image = CloudinaryField('image')
    description = models.TextField(max_length=1000)
    licence = models.CharField(
            max_length=50,
            choices=licence_type,
            default="All"
        )
    price = models.FloatField()

    class Meta:
        ordering = ['manufacturer', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug, 'pk': self.pk})


class Comment(models.Model):
    """
    This is a custom model
    """
    post = models.ForeignKey(
            Product, related_name="comments", on_delete=models.CASCADE
        )
    name = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date_added"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Order(models.Model):
    """
    Model taken from Dennis Ivy's tutorial - see README.md
    """
    customer = models.ForeignKey(
            Customer, on_delete=models.SET_NULL, null=True, blank=True
        )
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    """
    This is a custom model
    """
    transaction_id = models.ForeignKey(
            Order,
            related_name='orders_table',
            on_delete=models.SET_NULL,
            null=True,
            blank=True
        )
    customer = models.ForeignKey(
            Customer,
            related_name="customer_name",
            on_delete=models.SET_NULL,
            null=True,
            blank=True
        )
    product = models.ForeignKey(
            Product,
            on_delete=models.SET_NULL,
            null=True
        )
    price = models.ForeignKey(
            Product,
            related_name="item_price",
            on_delete=models.SET_NULL,
            null=True
        )
    order = models.ForeignKey(
            Order,
            on_delete=models.SET_NULL,
            null=True
        )
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    """
    Model taken from Dennis Ivy's tutorial - see README.md
    """
    customer = models.ForeignKey(
            Customer,
            on_delete=models.SET_NULL,
            null=True
        )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
