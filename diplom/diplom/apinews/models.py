from email.mime import image
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation

class ApiNews(models.Model):
    title = models.CharField(max_length=255 ,verbose_name='Название статьи', blank=False)
    description = models.CharField(max_length=255, verbose_name='Описание', blank=False)
    text = models.TextField(verbose_name='Текст', blank=False)
    time = models.DateTimeField(verbose_name='Время', auto_now=True)
    image = models.ImageField(verbose_name="Картинка", upload_to='img')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}|{self.title}'

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = 'Новости'

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(ApiNews, verbose_name="Пост", related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    time = models.DateTimeField(verbose_name='Время', auto_now=True)

    def __str__(self) -> str:
        return f'{self.user} | {self.post}'

    class Meta:
        verbose_name = "Комментарии"
        verbose_name_plural = 'Комментарии'

