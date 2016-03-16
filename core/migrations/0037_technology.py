# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20160303_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('vector', models.TextField(help_text=b'SVG contents. It is recommended to use a compressor and remove width/height attributes.')),
                ('label', models.CharField(max_length=255)),
                ('link', models.URLField(help_text=b'External URL of the Technology.', max_length=255, null=True, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='technologies', to='core.ServicesPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
