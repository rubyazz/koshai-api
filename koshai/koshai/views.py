from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserRegistrationForm


def main(request):
    return JsonResponse({"Hello": "world"})


class UserRegisterView(generic.CreateView):
    form_class = UserRegistrationForm
    template_name = "pages/register.html"
    success_url = reverse_lazy("home")
