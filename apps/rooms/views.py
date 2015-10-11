from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group as AuthGroup
from django.contrib.sites.models import RequestSite
from django.core import signing
from django.core.mail import send_mail
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import (FormView, UpdateView, CreateView,
                                       DeleteView)

from apps.accounts.mixins import LoggedInRequiredMixin
from apps.slots.models import TimeSlot
from .models import Room
from .forms import RoomCreateForm

class RoomSearch(LoggedInRequiredMixin, ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'room_search.html'

    def get_queryset(self, **kwargs):
        qs = Room.objects.all()
        # add searching
        return qs


class MyRooms(LoggedInRequiredMixin, ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'my_rooms.html'

    def get_queryset(self, **kwargs):
        qs = Room.objects.filter(user=self.request.user)
        # add searching
        return qs


class RoomDetail(LoggedInRequiredMixin, DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'room_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RoomDetail, self).get_context_data(**kwargs)
        context['spots'] = TimeSlot.objects.filter(room=self.object)
        return context


class RoomCreate(LoggedInRequiredMixin, CreateView):
    model = Room
    template_name = 'room_create.html'
    form_class = RoomCreateForm
    success_url = reverse_lazy('rooms:my-rooms')

    def get_form_kwargs(self):
        kwargs = super(RoomCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs