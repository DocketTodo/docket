from django.db import models

from apps.accounts.models import DocketUser

class Room(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(DocketUser)
    description = models.TextField(blank=True, null=True)