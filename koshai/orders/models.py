from django.db import models
from django.utils.translation import gettext_lazy as _
from restaurants.models import MenuItem


class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PROCESSING", "Processing"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    ]

    customer = models.ForeignKey(
        "customers.Customer", on_delete=models.CASCADE, related_name="orders"
    )
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


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def save(self, *args, **kwargs):
        if self.menu_item and self.menu_item.price is not None:
            self.price = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)
