from rest_framework import viewsets
from apinews.models import ApiNews
from apinews.serializers import SerializerMain, SerializerComment, SerializerCategry
from rest_framework.permissions import IsAuthenticated


class MainViewSet(viewsets.ModelViewSet):
    queryset = ApiNews.objects.all().order_by('title')
    serializer_class = SerializerMain

class MainCommentSet(viewsets.ModelViewSet):
    queryset = ApiNews.objects.all().order_by('title')
    serializer_class = SerializerComment

class MainCategorySet(viewsets.ModelViewSet):
    queryset = ApiNews.objects.all().order_by('title')
    serializer_class = SerializerCategry

