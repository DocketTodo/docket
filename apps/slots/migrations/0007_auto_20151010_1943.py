# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0006_timeslot_reserved'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='roomId',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='room',
            field=models.ForeignKey(blank=True, to='rooms.Room', null=True),
        ),
    ]
