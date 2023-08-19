from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser


class Restaurant(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("CLOSED", "Closed"),
    ]

    name = models.CharField(_("name"), max_length=100)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(_("address"))
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN",
    )

    def __str__(self):
        return self.name or self.user.email


class CategoryMenuItem(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        verbose_name = _("Menu Item Category")
        verbose_name_plural = _("Menu Item Categories")

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey("restaurants.Restaurant", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True
    )
    image = models.ImageField(
        _("image"), upload_to="menu/items/", blank=True, null=True
    )
    category = models.ForeignKey(CategoryMenuItem, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("Menu Item")
        verbose_name_plural = _("Menu Items")

    def __str__(self) -> str:
        return self.name
        