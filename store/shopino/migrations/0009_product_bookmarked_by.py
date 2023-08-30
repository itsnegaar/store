# Generated by Django 4.2.4 on 2023-08-30 11:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopino', '0008_remove_product_bookmarked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bookmarked_by',
            field=models.ManyToManyField(related_name='bookmarked_products', through='shopino.UserBookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]
