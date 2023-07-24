from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def whoami(request) -> Response:
    """Return the current Staff data."""
    return JsonResponse({"your": "name"})
