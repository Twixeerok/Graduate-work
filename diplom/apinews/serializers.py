from rest_framework import serializers
from apinews.models import ApiNews, Comment, Category


class SerializerCategry(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title')

class SerializerMain(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiNews
        exclude = []


class SerializerComment(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('text','time')