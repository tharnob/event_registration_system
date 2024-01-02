from rest_framework import serializers
from event_registration.models import RegisteredEvent




class RegSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = RegisteredEvent
        fields = ['id', 'event_id', 'event_title', 'user_name', 'created_at', 'url', 'owner']