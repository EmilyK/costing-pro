# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rawmaterial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlogin',
            old_name='username',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usersignup',
            old_name='username',
            new_name='email',
        ),
    ]
