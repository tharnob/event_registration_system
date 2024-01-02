from rest_framework import serializers
from events.models import Event




class EventSerializer(serializers.HyperlinkedModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'event_date', 'event_time', 'location_name', 'slot', 'created_at', 'url', 'owner']