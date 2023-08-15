from rest_framework import serializers
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    email = serializers.EmailField(validators=[], required=False)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "phone_number",
            "role",
            "first_name",
            "last_name",
            "nickname",
            "password",
            "last_login",
        )
