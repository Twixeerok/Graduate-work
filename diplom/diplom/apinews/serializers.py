from rest_framework import serializers
from apinews.models import ApiNews

class SerializerMain(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiNews
        fields = ('url','title','description', 'text', 'image')