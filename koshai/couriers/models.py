from django.db import models
from django.utils.translation import gettext_lazy as _

class Courier(models.Model):
    """
    Model to represent couriers.
    """
    phone = models.CharField(_("phone"), max_length=16)
    status = models.CharField(
        _("status"),
        max_length=32,
        choices=[
            ("AVAILABLE", "Available"),
            ("BUSY", "Busy"),
            ("OFFLINE", "Offline"),
        ],
        default="AVAILABLE",
    )
    coordinates = models.CharField(_("coordinates"), max_length=64, blank=True)

    class Meta:
        verbose_name = _("Courier")
        verbose_name_plural = _("Couriers")

    def __str__(self) -> str:
        return f"Courier {self.id}: {self.phone}"
