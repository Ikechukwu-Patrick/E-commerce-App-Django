from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField()
    home_address = models.TextField()
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=4)
    email_address = models.EmailField(max_length=200, unique=True)


class ProductCategory(models.Model):
    CATEGORY_CHOICES = [
        ('ELECTRONICS', 'Electronics'),
        ('GROCERIES', 'Groceries'),
        ('UTENSILS', 'Utensils'),
        ('CLOTHING', 'Clothing'),
        ('Gadget', 'gadget'),
        ('SHOES', 'shoes'),
        ('WRISTWATCHES', 'wristwatches'),
        ('DESIGNER GLASSES', 'designer glasses'),
    ]
    name = models.CharField(max_length=255, choices=CATEGORY_CHOICES)


class Product(models.Model):
    product_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


class Item(models.Model):
    name_of_product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shopping_cart')
    items = models.ManyToManyField(Item, related_name='carts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BillingInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='billing_info')
    address = models.TextField()
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customers')
    shopping_cart = models.OneToOneField(ShoppingCart, on_delete=models.SET_NULL, null=True, blank=True)


class Address(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=105)
    house_number = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


