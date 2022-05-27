from django.urls import path, include, re_path
from rest_framework import routers
from apinews.views import  MainViewSet

router = routers.DefaultRouter()
router.register(r'main', MainViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]