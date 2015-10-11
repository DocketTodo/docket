from django.db import models

from apps.rooms.models import Room
from apps.accounts.models import DocketUser

class TimeSlot(models.Model):
    room = models.ForeignKey(Room, blank=True, null=True)
    roomId = models.IntegerField()
    user = models.ForeignKey(DocketUser, blank=True, null=True)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()
    name = models.CharField(max_length=255, blank=True, null=True)
    reserved = models.BooleanField(default=False)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return 'Unnamed reservation'

    def save(self, force_insert=False, force_update=False, **kwargs):
        self.reserved = not not self.user
        self.room = Room.objects.get(id=self.roomId)
        return super(TimeSlot, self).save(force_insert=False, **kwargs)