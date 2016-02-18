# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20160218_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpage',
            name='client_external_url',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
