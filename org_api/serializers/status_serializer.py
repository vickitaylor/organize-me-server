from rest_framework import serializers
from org_api.models import Status

class StatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Status
        fields = ('id', 'title')
