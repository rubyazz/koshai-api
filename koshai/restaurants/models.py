from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser


class Restaurant(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("CLOSED", "Closed"),
    ]

    name = models.CharField(_("name"), max_length=100)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, unique=True, default=1
    )
    address = models.TextField(_("address"))
    status = models.CharField(
        _("status"),
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN",
    )

    def __str__(self):
        return self.name
