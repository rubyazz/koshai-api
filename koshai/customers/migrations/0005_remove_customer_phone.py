# Generated by Django 4.2.3 on 2023-08-13 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_remove_customer_order_alter_customer_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
