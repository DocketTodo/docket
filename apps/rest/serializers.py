from django.core.exceptions import PermissionDenied

from rest_framework import routers, serializers, viewsets

from apps.rooms.models import Room
from apps.slots.models import TimeSlot

class RoomSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    slots = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('username', 'name', 'description', 'slots', )

    def get_username(self, obj):
        return obj.user.username

    def get_slots(self, obj):
        return [{
            'id': t.id,
            'user': t.user.username,
            's_time': t.start_dt,
            'e_time': t.end_dt
        } for t in TimeSlot.objects.filter(room=obj)]

    # def update(self, instance, validated_data):
    #     get = validated_data.get
    #     if self.context['request'].user == instance.user:
    #         instance.data = get('data', instance.data)
    #         instance.save()
    #         return instance
    #     raise PermissionDenied


class TimeSlotSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = TimeSlot
        fields = ('username', 'start_dt', 'end_dt', 'room', )

    def get_username(self, obj):
        return obj.user.username