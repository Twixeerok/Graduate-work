from django.contrib import admin
from apinews.models import ApiNews, Comment, Category

admin.site.register(ApiNews)
admin.site.register(Category)
admin.site.register(Comment)

