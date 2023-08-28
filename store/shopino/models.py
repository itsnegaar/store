from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    objects = None
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200)
    description = models.TextField()
    followers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    bookmarked_by = models.ManyToManyField(User, related_name='bookmarked_products')


    def __str__(self):
        return self.name

