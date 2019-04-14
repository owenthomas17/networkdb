from rest_framework.response import Response
from rest_flex_fields import FlexFieldsModelViewSet
from rest_api.serializers import DevicesSerializer
from rest_api.serializers import SitesSerializer
from rest_api.models import Devices
from rest_api.models import Sites

class DevicesViewSet(FlexFieldsModelViewSet):
    """
    API endpoint
    """
    serializer_class = DevicesSerializer	
    queryset = Devices.objects.all()
    permit_list_expands = ['site']

class SitesViewSet(FlexFieldsModelViewSet):
    """
    API endpoint
    """
    serializer_class = SitesSerializer	
    queryset = Sites.objects.all()
