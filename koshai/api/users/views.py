from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(["GET"])
def whoami(request):
    """Return the current User data."""

    user = request.user
    if not user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    serializer = UserSerializer(user)
    return Response(status=status.HTTP_200_OK, data=serializer.data)
