from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class PhoneNumberModelBackend(ModelBackend):
    """used for authenticate by using phone_number"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        phone_number = kwargs.get("phone_number")
        if phone_number:
            try:
                user = UserModel._default_manager.get(phone_number=phone_number)
            except UserModel.DoesNotExist:
                UserModel().set_password(password)
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user