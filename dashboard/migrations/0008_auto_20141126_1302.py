# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20141126_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersignup',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='usersignup',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
