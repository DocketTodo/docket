from django.db import models

from apps.rooms.models import Room
from apps.accounts.models import DocketUser

class TimeSlot(models.Model):
    room = models.ForeignKey(Room)
    user = models.ForeignKey(DocketUser, blank=True, null=True)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return 'Unnamed reservation'