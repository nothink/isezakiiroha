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
