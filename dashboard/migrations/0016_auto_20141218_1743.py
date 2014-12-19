# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_pricing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='product_raw_materials',
        ),
        migrations.DeleteModel(
            name='Pricing',
        ),
    ]
