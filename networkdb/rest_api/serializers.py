from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from rest_api.models import Devices
from rest_api.models import Sites

class SitesSerializer(FlexFieldsModelSerializer):
    '''
    '''

    class Meta:
        model = Sites
        fields = '__all__'

class DevicesSerializer(FlexFieldsModelSerializer):
    '''
    '''

    class Meta:
        model = Devices
        fields = '__all__'

    expandable_fields = {
            'site': (SitesSerializer, {'source': 'site'})
    }
