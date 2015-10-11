from django.core.exceptions import PermissionDenied

from rest_framework import routers, serializers, viewsets

from apps.rooms.models import Room
from apps.slots.models import TimeSlot

class RoomSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    slots = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('username', 'name', 'description', 'slots', 'rating', )

    def get_username(self, obj):
        if obj.user:
            return obj.user.username
        else:
            return None

    def get_slots(self, obj):
        return [{
            'id': t.id,
            'user': t.user.username,
            's_time': t.start_dt,
            'e_time': t.end_dt
        } for t in TimeSlot.objects.filter(room=obj)]


class TimeSlotSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSlot
        fields = ('name', 'user', 'start_dt', 'end_dt', 'room', )

    # def get_username(self, obj):
    #     if obj.user:
    #         return obj.user.username
    #     else:
    #         return None

    # def update(self, instance, validated_data):
    #     get = validated_data.get
    #     print validated_data
    #     raise PermissionDenied


class TimeSlotCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeSlot
        fields = ('name', 'start_dt', 'end_dt', 'room', )

    def create(self, kwargs):
        kwargs['user'] = self.context['request'].user
        t = TimeSlot.objects.create(**kwargs)
        t.save()
        return t