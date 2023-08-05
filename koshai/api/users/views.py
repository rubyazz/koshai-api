from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def whoami(request) -> JsonResponse:
    """Return the current User data."""
    return JsonResponse({"your": "name"})
