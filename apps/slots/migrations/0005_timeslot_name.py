# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0004_auto_20151010_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
