from rest_framework import viewsets  # , permissions

from project.app.models import Resource
from project.app.serializers import ResourceSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    """
    vcardリソース用のViewSet
    """

    queryset = Resource.objects.all().order_by("-created")
    serializer_class = ResourceSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        """
        シリアライザの取得
        ここではdataの戦闘が配列の時にmany=Trueを指定する
        """
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super(ResourceViewSet, self).get_serializer(*args, **kwargs)
