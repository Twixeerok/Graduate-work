from django.urls import path, include, re_path
from rest_framework import routers
from apinews.views import  MainViewSet, MainCategorySet, MainCommentSet

router = routers.DefaultRouter()
router.register(r'main', MainViewSet, 'main')
router.register(r'main', MainCategorySet, 'main')
router.register(r'comment', MainCommentSet, 'comment')



urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] 
