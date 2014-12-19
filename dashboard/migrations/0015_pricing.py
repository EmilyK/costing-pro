# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_product_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estimated_price', models.IntegerField(default=0)),
                ('product_raw_materials', models.ManyToManyField(to='dashboard.ProductRawMaterial')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
