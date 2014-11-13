# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('division', models.CharField(max_length=20)),
                ('parish', models.CharField(max_length=20)),
                ('village', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=15, choices=[(b'CRAFTS', b'Crafts')])),
                ('telephone_number', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
