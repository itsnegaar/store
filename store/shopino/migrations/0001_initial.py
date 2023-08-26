# Generated by Django 4.2.4 on 2023-08-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShopName', models.CharField(max_length=100, unique=True)),
                ('ShopAddress', models.CharField(max_length=200)),
                ('ShopDescription', models.TextField()),
            ],
        ),
    ]