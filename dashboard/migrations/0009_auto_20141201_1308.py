# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rawmaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='cost',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rawmaterial',
            name='size',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=3),
            preserve_default=True,
        ),
    ]
