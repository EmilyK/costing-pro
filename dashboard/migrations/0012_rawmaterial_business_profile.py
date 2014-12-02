# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='business_profile',
            field=models.ForeignKey(blank=True, to='dashboard.BusinessProfile', null=True),
            preserve_default=True,
        ),
    ]
