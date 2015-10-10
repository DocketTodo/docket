# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0003_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='end_dt',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 21, 18, 26, 173000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timeslot',
            name='start_dt',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 21, 18, 26, 173000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
