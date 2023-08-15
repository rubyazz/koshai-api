from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser


def validate_image_file_size(image):
    max_size = 1024 * 1024  # 1MB

    if image.size > max_size:
        raise ValidationError("File size should not exceed 1MB.")


class Customer(models.Model):
    full_name = models.CharField(
        _("Full Name"),
        max_length=255,
        null=True,
    )
    address = models.TextField(_("address"))
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(
        _("Avatar"),
        upload_to="customer/avatars/",
        blank=True,
        null=True,
        help_text=_("Upload an avatar image (max 1MB)."),
        max_length=1024,
        validators=[validate_image_file_size],
    )
    is_active = models.BooleanField(_("active"), default=True)

    def __str__(self):
        return (
            self.full_name or self.user.email
        )  # Change to the appropriate field for display
