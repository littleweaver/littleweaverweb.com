# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_opengraphandmetasettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opengraphandmetasettings',
            options={'verbose_name': 'Head Meta'},
        ),
        migrations.AddField(
            model_name='opengraphandmetasettings',
            name='ga_id',
            field=models.CharField(help_text=b'Google Analytics Tracking ID, e.g. UA-12345678-1', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='opengraphandmetasettings',
            name='meta_description',
            field=models.CharField(help_text=b'meta[name="description"] and og:description', max_length=255),
        ),
    ]
