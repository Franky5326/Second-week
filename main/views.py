from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import RegisterUserForm


def home(request):
    return render(request, 'users/home.html')


class SignUp(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def profile(request):
    return render(
        request,
        'registration/profile.html'
    )
