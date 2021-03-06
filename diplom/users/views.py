from django.shortcuts import render
from django.views.generic import TemplateView, FormView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from users.forms import AccountForm, CustomUserForm
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import make_password

class Registrations(FormView):
    template_name = 'django_registration/registration_form.html'
    form_class = AccountForm
    success_url = reverse_lazy('category:mainpage')

    def form_valid(self, form):
        form = form.save(commit=False)
        user = form
        form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())