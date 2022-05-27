from rest_framework import viewsets
from apinews.models import ApiNews
from apinews.serializers import SerializerMain
from rest_framework.permissions import IsAuthenticated


class MainViewSet(viewsets.ModelViewSet):
    queryset = ApiNews.objects.all().order_by('title')
    serializer_class = SerializerMain

