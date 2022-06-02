from django.contrib import admin
from apinews.models import ApiNews, Comment, Category, Like

admin.site.register(ApiNews)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)

