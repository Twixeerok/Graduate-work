from django.contrib import admin
from django.urls import path
from news.views import MainPageView, PostNews, News, Profile, ProfileEdit
from .decorators import check_recaptcha

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('add/', check_recaptcha(PostNews.as_view()), name='add'),
    path('<int:id>/', News.as_view(), name='news'),
    path('profile/edit/', check_recaptcha(ProfileEdit.as_view()), name='profiledit'),
    path('profile/', Profile.as_view(), name='profile'),
]



