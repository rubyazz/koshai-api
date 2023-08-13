from rest_framework_simplejwt.views import TokenViewBase

from api.restauth.serializers import LoginSerializer


class ObtainTokenView(TokenViewBase):
    """this class using for authenticate with TokenViewBase and serialize it"""

    serializer_class = LoginSerializer