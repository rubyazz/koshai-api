from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser


class Courier(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # new field
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
    first_name = models.CharField(_("first name"), max_length=100, null=True)
    last_name = models.CharField(_("last name"), max_length=100, null=True)
    coordinates = models.PointField(
        _("coordinates"),
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"Courier: {self.first_name}" or self.user.email
