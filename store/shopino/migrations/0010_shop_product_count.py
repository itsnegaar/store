# Generated by Django 4.2.4 on 2023-08-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopino', '0009_product_bookmarked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='product_count',
            field=models.IntegerField(default=0),
        ),
    ]
