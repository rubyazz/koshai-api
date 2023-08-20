from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
    phone_number = forms.CharField(max_length=32, label="Phone number", required=False)

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "phone_number",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "nickname",
            "role",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs["class"] = "form-control"
