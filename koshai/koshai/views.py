from django.http import JsonResponse

def main(request):
    return JsonResponse({"Hello": "world"})