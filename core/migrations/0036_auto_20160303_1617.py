# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('core', '0035_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opengraphandmetasettings',
            name='open_graph_image_path',
        ),
        migrations.AddField(
            model_name='opengraphandmetasettings',
            name='open_graph_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='opengraphandmetasettings',
            name='ga_id',
            field=models.CharField(help_text=b'Google Analytics Tracking ID, e.g., UA-12345678-1', max_length=30, null=True, blank=True),
        ),
    ]
