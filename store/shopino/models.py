from django.db import models
from django.core.validators import MinLengthValidator

class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # address = models.CharField(max_length=200, validators=[MinLengthValidator(5, "Shop name must be at least 5 characters long")] )
    address = models.CharField(max_length=200)

    description = models.TextField()
    followers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

