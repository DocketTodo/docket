# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0005_timeslot_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]
