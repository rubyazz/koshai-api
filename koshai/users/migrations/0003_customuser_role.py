# Generated by Django 4.2.3 on 2023-08-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_img_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('restaurant', 'Restaurant'), ('courier', 'Courier'), ('customer', 'Customer')], default='customer', max_length=20),
        ),
    ]
