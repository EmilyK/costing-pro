# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20141218_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='original_size',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
    ]
