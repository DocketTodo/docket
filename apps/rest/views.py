from django.http import HttpResponseForbidden

from rest_framework import generics, status
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.rooms.models import Room
from apps.slots.models import TimeSlot

from .serializers import RoomSerializer, TimeSlotSerializer, TimeSlotCreateSerializer

class RoomDetail(SessionAuthentication, generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return Room.objects.get(
            id=self.kwargs['pk'])


class TimeSlotCreate(SessionAuthentication, generics.CreateAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotCreateSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated,)


class TimeSlotDetail(SessionAuthentication, generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return TimeSlot.objects.get(
            id=self.kwargs['pk'])