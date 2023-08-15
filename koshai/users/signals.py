from couriers.models import Courier
from customers.models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver
from restaurants.models import Restaurant
from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def create_related_objects(sender, instance, created, **kwargs):
    if created:
        if instance.role == "courier":
            Courier.objects.create(user=instance)
        elif instance.role == "restaurant":
            Restaurant.objects.create(user=instance)
        elif instance.role == "customer":
            Customer.objects.create(user=instance)
