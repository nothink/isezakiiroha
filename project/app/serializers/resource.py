from rest_framework import serializers

from project.app.models import Resource


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    """
    vcardリソース用のモデルシリアライザ
    """

    class Meta:
        model = Resource
        fields = ["key", "url", "fetched", "created"]
