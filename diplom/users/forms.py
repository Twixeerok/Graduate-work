from django_registration.forms import RegistrationForm
from django import forms
from users.models import User


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User

class AccountForm(RegistrationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'patronymic', 'avatar', 'instagram', 'twitter', 'facebook', 'description']
   