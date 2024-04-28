from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")  # Using reverse_lazy instead of reverse
    template_name = "accounts/signup.html"
