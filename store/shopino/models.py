from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=100 , unique=True)
    shop_address = models.CharField(max_length=200)
    shop_description = models.TextField()


    def __str__(self):
        return self.shop_name
