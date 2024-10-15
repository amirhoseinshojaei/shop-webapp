from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True,unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField(region="US")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    # Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    # Calculate discount percentage
    def discount_percentage(self):
        if self.is_sale and self.sale_price < self.price:
            discount = (self.price - self.sale_price) / self.price * 100
            return round(discount, 0)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=500)
    phone = PhoneNumberField(region="US")
    date_ordered = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)
