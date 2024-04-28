from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import CreateView
from . import forms

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        # Log out the user for GET requests
        logout(request)
        return redirect(reverse_lazy('login'))

    def post(self, request, *args, **kwargs):
        # Log out the user for POST requests
        logout(request)
        return redirect(reverse_lazy('login'))

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")  # Using reverse_lazy instead of reverse
    template_name = "accounts/signup.html"