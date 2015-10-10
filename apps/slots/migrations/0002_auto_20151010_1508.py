# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='room',
        ),
        migrations.RemoveField(
            model_name='timeslot',
            name='user',
        ),
        migrations.DeleteModel(
            name='TimeSlot',
        ),
    ]
