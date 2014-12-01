# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20141126_1302'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLogin',
        ),
        migrations.DeleteModel(
            name='UserSignUp',
        ),
    ]
