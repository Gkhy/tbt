# Generated by Django 3.2.13 on 2022-11-18 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_quantiy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quantiy',
            new_name='quantity',
        ),
    ]
