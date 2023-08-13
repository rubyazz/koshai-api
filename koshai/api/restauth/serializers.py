from api.users.serializers import UserSerializer
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenVerifySerializer,
)
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken, Token


class KoshaiTokenObtainPairSerializer(TokenObtainPairSerializer):
    @property
    def validated_data(self):
        """
        Additionally put User data to avoid followed request to fetch them.
        """

        validated_data = super().validated_data
        user = self.user
        validated_data["user"] = UserSerializer(instance=user).data

        return validated_data


class KoshaiTokenVerifySerializer(TokenVerifySerializer):
    @property
    def validated_data(self):
        validated_data = super().validated_data
        Token()
        return validated_data


class LoginSerializer(KoshaiTokenObtainPairSerializer):
    """
    This class used for serialize auth credentials by Backend classes,
    validate method for checking login field for is this field email or phone_number
    and give to authenticate
    """

    username_field = "login"

    def is_email(self, login: str) -> bool:
        try:
            validate_email(login)
            return True
        except ValidationError:
            return False

    def validate(self, attrs):
        login = attrs["login"]

        login_field_name = "email" if self.is_email(login) else "phone_number"

        authenticate_kwargs = {
            login_field_name: login,
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        refresh = RefreshToken.for_user(self.user)
        access = refresh.access_token

        tokens_data = {
            "refresh": str(refresh),
            "access": str(access),
        }

        return tokens_data
