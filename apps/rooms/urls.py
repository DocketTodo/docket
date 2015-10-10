from django.conf.urls import patterns, include, url

from .views import RoomSearch, RoomDetail, RoomCreate, MyRooms

urlpatterns = patterns('',
    url(r'search/?$', RoomSearch.as_view(), name='room-search'),
    url(r'create/?$', RoomCreate.as_view(), name='room-create'),
    url(r'mine/?$', MyRooms.as_view(), name='my-rooms'),
    url(r'room/(?P<pk>\d+)/?$', RoomDetail.as_view(), name='room-detail'),
)