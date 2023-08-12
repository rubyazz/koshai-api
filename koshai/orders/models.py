from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PROCESSING", "Processing"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    ]

    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE)
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )
    courier = models.ForeignKey(
        "couriers.Courier", on_delete=models.SET_NULL, null=True, blank=True
    )
    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
