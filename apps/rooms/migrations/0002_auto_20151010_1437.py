# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='listcategory',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='listcategory',
            name='user',
        ),
        migrations.DeleteModel(
            name='ListCategory',
        ),
    ]
