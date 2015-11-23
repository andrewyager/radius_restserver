# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeradius', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdata',
            options={'ordering': ['username', 'date', 'data_hour'], 'managed': False},
        ),
    ]
