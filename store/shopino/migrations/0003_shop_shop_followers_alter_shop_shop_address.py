# Generated by Django 4.2.4 on 2023-08-26 08:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopino', '0002_rename_shopaddress_shop_shop_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_followers',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_address',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(5, 'Shop name must be at least 5 characters long')]),
        ),
    ]