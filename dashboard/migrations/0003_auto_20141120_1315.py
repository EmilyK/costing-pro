# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20141118_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='telephone_number',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
    ]
