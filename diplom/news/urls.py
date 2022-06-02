from django.contrib import admin
from django.urls import path
from news.views import MainPageView, PostNews, News, Profile, ProfileEdit, MainView, Search, Likes, RemoveLike, UserProfile
from .decorators import check_recaptcha


app_name = 'category'

urlpatterns = [
    path('', MainView.as_view(), name='mainpage'),
    path('news/<slug:slug>/', MainPageView.as_view(), name='main'),
    path('add/', check_recaptcha(PostNews.as_view()), name='add'),
    path('<int:id>/', News.as_view(), name='news'),
    path('user/<int:id>/', UserProfile.as_view(), name='userprof'),
    path('accounts/profile/edit/', check_recaptcha(ProfileEdit.as_view()), name='profiledit'),
    path('accounts/profile/', Profile.as_view(), name='profile'),
    path('search/', Search.as_view(), name='search'),
    path('add/like', Likes.as_view(), name='adds'),
    path('remove/', RemoveLike.as_view(), name='remove'),
]



