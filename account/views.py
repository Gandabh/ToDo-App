from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_text
from django.contrib.auth import get_user_model
from account.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from account.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView
from account.forms import RegistrationForm, LoginForm

User = get_user_model()




class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('account:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('http://127.0.0.1:8000/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)



class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('http://127.0.0.1:8000/')
        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)


def logout(request):
    django_logout(request)
    return redirect('/')
