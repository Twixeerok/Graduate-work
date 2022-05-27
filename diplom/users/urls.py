from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from users.forms import CustomUserForm
from django.conf import settings
from django.conf.urls.static import static
from users.views import Registrations

urlpatterns = [
    path('accounts/register/', Registrations.as_view(), name='django_registration'),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
