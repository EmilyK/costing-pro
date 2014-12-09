# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_rawmaterial_business_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Product name')),
                ('product_size', models.CharField(max_length=8, choices=[(b's', b'Small'), (b'm', b'Medium'), (b'l', b'Large')])),
                ('business_profile', models.ForeignKey(blank=True, to='dashboard.BusinessProfile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductRawMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(default=1)),
                ('business_profile', models.ForeignKey(blank=True, to='dashboard.BusinessProfile', null=True)),
                ('product', models.ForeignKey(to='dashboard.Product')),
                ('raw_material', models.ForeignKey(to='dashboard.RawMaterial')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='rawmaterial',
            name='time_rate',
            field=models.CharField(max_length=50, choices=[(b'd', b'Daily'), (b'w', b'Weekly'), (b'm', b'Monthly')]),
            preserve_default=True,
        ),
    ]
