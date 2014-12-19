# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('telephone_number', models.CharField(max_length=10)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Product name')),
                ('product_size', models.CharField(max_length=8, choices=[(b's', b'Small'), (b'm', b'Medium'), (b'l', b'Large')])),
                ('created', models.BooleanField(default=False)),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_rate', models.CharField(max_length=50, choices=[(b'd', b'Daily'), (b'w', b'Weekly'), (b'm', b'Monthly')])),
                ('name', models.CharField(max_length=50)),
                ('original_size', models.DecimalField(default=0.0, max_digits=10, decimal_places=3)),
                ('size', models.DecimalField(default=0.0, max_digits=10, decimal_places=3)),
                ('cost', models.DecimalField(default=0.0, max_digits=50, decimal_places=5)),
                ('business_profile', models.ForeignKey(blank=True, to='dashboard.BusinessProfile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='productrawmaterial',
            name='raw_material',
            field=models.ForeignKey(to='dashboard.RawMaterial'),
            preserve_default=True,
        ),
    ]
