# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20141205_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
