from django.conf.urls import patterns, include, url

from .views import MyReservations

urlpatterns = patterns('',
    url(r'mine/?$', MyReservations.as_view(), name='my-reservations'),
)