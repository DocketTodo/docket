# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_room_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
