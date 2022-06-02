from django.db import models


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from users.managers import UserManager


class User(AbstractUser):
    username = models.CharField(_('username'), unique=True, max_length=255)
    password = models.CharField(_('password'), max_length=128)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=30, blank=False)
    patronymic = models.CharField(_('Отчество'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(verbose_name="Аватар", upload_to='avatars/', default='default.png', blank=True)
    is_staff = models.BooleanField(_('Администратор'), default=True)
    instagram = models.CharField(verbose_name="Инстаграм", max_length=100, blank=True)
    twitter = models.CharField(verbose_name='Тветтер', max_length=100, blank=True)
    facebook = models.CharField(verbose_name='Фейсбук', max_length=100, blank=True)
    vk = models.CharField(verbose_name='Вк', max_length=100, blank=True)
    description = models.CharField(max_length=150, verbose_name='Описание', blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = f"{self.last_name} {self.first_name} {self.patronymic}"
        return full_name.strip()
