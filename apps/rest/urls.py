from django.conf.urls import patterns, include, url

from .views import RoomDetail, TimeSlotDetail, TimeSlotCreate

urlpatterns = patterns('',
    url(r'rooms/room/(?P<pk>\d+)/?$', RoomDetail.as_view(), name='room-detail'),
    url(r'slots/slot/(?P<pk>\d+)/?$', TimeSlotDetail.as_view(), name='slot-detail'),
    url(r'slots/slot/?$', TimeSlotCreate.as_view(), name='slot-create'),
)